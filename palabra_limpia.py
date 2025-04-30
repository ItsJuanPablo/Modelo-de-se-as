# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:11:06 2025

@author: jp00c
"""

import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import pickle
import time

model = tf.keras.models.load_model('modelo_mediapipe_letras.h5')
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

current_word = ""
last_letter = ""
words = []
last_detected_time = time.time()
last_capture_time = 0
same_letter_counter = 0
stable_threshold = 3
capture_interval = 1.0

def predict_letter(landmarks):
    landmarks = np.array(landmarks).flatten().reshape(1, -1)
    prediction = model.predict(landmarks)
    predicted_label = np.argmax(prediction)
    return label_encoder.inverse_transform([predicted_label])[0]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    current_time = time.time()

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            letter = predict_letter(landmarks)
            print("Letra detectada:", letter)

            if letter == last_letter:
                same_letter_counter += 1
            else:
                same_letter_counter = 1  # comienza nuevo conteo
                last_letter = letter

            # Capturar letra si es estable o si cambia y ha pasado tiempo
            if same_letter_counter >= stable_threshold and (current_time - last_capture_time > capture_interval):
                current_word += letter
                last_detected_time = current_time
                last_capture_time = current_time
                same_letter_counter = 0
                print("Letra añadida:", letter)

    else:
        last_letter = ""
        same_letter_counter = 0

    if current_word and (current_time - last_detected_time > 3):
        words.append(current_word)
        current_word = ""
        last_letter = ""

    cv2.putText(frame, f"Palabra actual: {current_word}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    y_offset = 60
    for idx, palabra in enumerate(words[-5:]):
        cv2.putText(frame, f"{idx+1}: {palabra}", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
        y_offset += 30

    cv2.imshow('Reconocimiento de Senas', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 13:  # Enter
        if current_word:
            words.append(current_word)
            current_word = ""
            last_letter = ""

    if key == 8:  # Backspace
        current_word = current_word[:-1]

    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
