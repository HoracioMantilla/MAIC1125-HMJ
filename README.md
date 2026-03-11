# MAIC1125-HMJ
Detección de elementos de protección personal EPP (Proyectos de construcción)

# ADVERTENCIA
Este modelo es una herramienta de apoyo solo para screening preliminar. 
Produce falsos negativos. NO debe usarse como único verificador en decisiones
de seguridad vital.

# DESCRIPCIÓN DEL DATASET
Cantidad de imagenes inciales 113 (distribución 70/20/10)
Preproceso: Autorientación
Augmentation
  Resultados por ejemplo de entrenamiento: 3
  Recorte (Crop): Zoom mínimo 0%, Zoom máximo 20%
  Brillo (Brightness): Entre -15% y +15%
  Cantidad final de imagenes del data set 271
Metricas:
  mAp@50 61.9%
  Precisión 66%
  Recall 58.1%

El dataset contiene un desbalance importante en cantidad de etiquetas sin casco (no helmet),
aunque se dió prioridad a imagenes de proyectos en construcción se tuvo que complementar con
fotografías en otros ambientes con el fin de lograr algo de balance y mejorar el modelo

# QUICK START
Para acceder al visor 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HoracioMantilla/MAIC1125-HMJ/blob/main/1_Cuadernos/02_Inferencia.ipynb)

