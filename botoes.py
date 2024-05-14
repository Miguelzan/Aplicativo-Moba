import requests
import json

# IMAGEM
from kivy.uix.image import Image

# LABEL
from kivy.uix.label import Label

# COMPORTAMENTO DE BOTÃO
from kivy.uix.button import ButtonBehavior


# Cria uma  imagem com comportamento de botão

class ImageButton(ButtonBehavior,Image):
    pass


# Cria um Texto com comportamento de botão

class LabelButton(ButtonBehavior,Label):
    pass
