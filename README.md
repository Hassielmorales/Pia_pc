Esta herramienta es una recopilación de aprendizajes obtenidos durante el curso de ciberseguridad. Su propósito es brindar ejemplos prácticos para aprender y practicar scripts relacionados con la seguridad informática, inspirados en las herramientas vistas en clase y desarrolladas en Python. Antes de ejecutar los scripts, se recomienda tener a la mano las rutas de las carpetas donde se trabajará. Algunos scripts requieren rutas específicas para guardar o leer archivos.

Web Scraping de Imágenes
Script diseñado para descargar imágenes en su tamaño original desde una página web. Librerías necesarias: beautifulsoup4, lxml. Uso: proporciona una URL de una página web y una ruta local donde se guardarán las imágenes. Ejemplo: URL: https://es.wikipedia.org/wiki/Imagen Ruta: C:\Users\JALCY\Desktop\

Screenshot por Email
Script para capturar pantallas y enviarlas por correo, útil para monitoreo rápido. Puede ejecutarse desde una USB. Librerías necesarias: email.mime, smtplib, pyscreenshot. Uso: proporciona una ruta con nombre y extensión de la imagen. Ejemplo: C:\Users\JALCY\Desktop\pc\screenshot.jpg

Comparativa de Hashes
Dos scripts que permiten generar y comparar hashes de archivos para verificar integridad. Librerías necesarias: hashlib, argparse. Uso: el primer script genera los hashes de dos archivos, el segundo compara los hashes para verificar si los archivos son idénticos.

Metadata de Imágenes
Script para extraer metadatos de imágenes almacenadas en una carpeta. Librería necesaria: Pillow

Estructura del repositorio
Pia_pc/
├── HashArchivo.py
├── HashCompare.py
├── meta.py
├── scraps.py
├── scrimagenes.py
├── screenshot.py
└── instrucciones.txt

Requisitos generales

Asegúrate de tener instalado Python 3.x y las siguientes librerías:
pip install beautifulsoup4 lxml pyscreenshot Pillow

