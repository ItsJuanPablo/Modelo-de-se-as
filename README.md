# Modelo-de-señas

Este trabajo se hizo con la intención y objetivo que de por medio de la cámara de un computador se pudiera captar el lenguaje de señas colombiano en tiempo real y de esta manera la persona que estaría comunicándose por medio de señas vea reflejado lo que quiere decir en la pantalla para así comunicarse asertivamente con una persona que no tenga un conocimiento y/o interpretación completo del lenguaje de señas.

Sobre la parte técnica se tiene que decir que por medio de un data set de imágenes de las letras del abecedario con su respectiva seña de lenguaje, con esto se llevó a cabo la alimentación y entrenamiento de un modelo de inteligencia artificial que aprende a identificar los patrones de las manos para así identificar las letras y por medio de un script de Python se usó ese modelo entrenado para reconocer las señas que se realizaban en tiempo real al captar con la cámara del PC las señas que se realizaban y reflejarlas en la pantalla.

A continuación se tienen todas las partes que conforman el proceso que se llevó a cabo para realizar este trabajo.

# Datasets
  Nuevamente mencionamos la parte central del aprendizaje, este banco de imagenes cuenta con 1 carpeta para cada letra del abecedario, y en cada carpeta hay fotos de personas haciendo la seña que representa esa letra.

# Codigos
  Ahora tenemos la parte operativa el cual se compone de un codigo en google Collab, y un ejecutable en Python.
  
  # Código de Google Collab:
  ![image](https://github.com/user-attachments/assets/13d8c659-7021-4bfc-8428-9ef2ee142e7e)
  
    Este codigo estara añadido a este repositorio bajo el nombre de: Modelo de letras, con la extensión: .ipynb
  
  Este código entrena un modelo de aprendizaje profundo para el reconocimiento de gestos manuales a partir de imágenes, utilizando la biblioteca MediaPipe para extraer puntos clave (landmarks) de las manos. Primero, instala las dependencias necesarias, luego monta Google Drive para acceder a un dataset organizado en carpetas de entrenamiento, validación y prueba. A partir de las imágenes del dataset, extrae características (coordenadas 3D de 21 puntos por mano), las etiqueta, codifica y divide en conjuntos de entrenamiento y validación. Luego crea una red neuronal con TensorFlow, la entrena, guarda el modelo entrenado y el codificador de etiquetas, y finalmente grafica la precisión del entrenamiento y validación a lo largo de las épocas.
  Al final guarda tanto el modelo (modelo_mediapipe_letras.h5) como el codificador de etiquetas (label_encoder.pkl) para su uso posterior.
  En la parte técnica el modelo tuvo un comportamiento adecuado al entrenarlo durante 50 épocas.
  
  ![image](https://github.com/user-attachments/assets/bae1de24-f689-4c20-a0c3-a8d9b5359b64)

  # Código de Python:
  ![image](https://github.com/user-attachments/assets/05743838-f34f-467c-bb46-9ee78eda3f99)
  
    Este codigo estara añadido a este repositorio bajo el nombre de: palabra_limpia, con la extensión: .py
    
  Este código permite realizar el reconocimiento de letras en tiempo real a través de gestos con las manos utilizando una cámara web. El sistema carga un modelo previamente entrenado (`modelo_mediapipe_letras.h5`) junto con su codificador de etiquetas (`label_encoder.pkl`) para interpretar los movimientos captados. Utilizando MediaPipe, detecta los puntos clave de la mano y, mediante el modelo, predice la letra correspondiente. Si una letra se mantiene estable durante un tiempo, se añade a una palabra que se va construyendo en pantalla. Además, el sistema permite mostrar las últimas palabras detectadas y ofrece opciones interactivas al usuario, como confirmar palabras con la tecla Enter o borrar letras con Backspace, todo mostrado visualmente mediante OpenCV.

# Resultados
![Captura de pantalla (119)](https://github.com/user-attachments/assets/8b37d823-fb2b-4171-a886-3d1164312021)

Aquí vemos la interfaz que se mostrara al usuario con la palabra ya escrita.

![image](https://github.com/user-attachments/assets/d1930564-57b8-488a-be2a-6c320cb69a8e)

# Recomendaciones
  Como recomendaciones finales se sugiere adaptar la ia para que permita aceptar letras del lenguaje de señas que se realicen con movimiento, ya que al ser videos se tiene que segmentar en frames que despues se tienen que procesar con un nuevo modelo de entrenamiento.


  

  

    
