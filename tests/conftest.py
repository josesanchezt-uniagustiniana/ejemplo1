import sys
import os

# Esto añade la carpeta raíz (ejemplo1) al sistema de rutas de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))