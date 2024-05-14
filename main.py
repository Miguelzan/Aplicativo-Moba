#Importa kivy

from kivy.app import App

#importa Builder
from kivy.lang import Builder

#Importando telas
from telas import *

#Importando botões
from botoes import *

#Importaum requisição
import requests
import json

#importando firebase
from myfirebase import MyFireBase

#Cria App

GUI = Builder.load_file("kv/main.kv")

#Cria funcionalidades do App

class DIGNUS_ESTApp(App):
    id_usuario = 1

    def build(self):
        self.firebase = MyFireBase()
        return GUI
#Mudando foto de perfil
    #def on_start(self):
        #requisicao = requests.get(f'https://aplicativodignusest-default-rtdb.firebaseio.com/{self.local_id}.json')
        #req_dic = requisicao.json()
        #avatar = req_dic['avatar']
        #foto_perfil = self.root.ids['foto_perfil']
        #foto_perfil.source = f'icones/{avatar}'

    #Carregar informações do usuario
    def open_info_user(self):
        try:
            with open('refreshtoken.txt','r') as arquivo:
                refresh_token = arquivo.read()
            local_id, id_token = self.firebase.trocar_token(refresh_token)
            self.local_id = local_id
            self.id_token = id_token

            requisicao = requests.get(f'https://aplicativodignusest-default-rtdb.firebaseio.com/{self.local_id}.json')
            requisicao_dic = requisicao.json()

            self.mudar_tela('tela1')
        except:
            pass


    #Cria a função de mudar de tela
    def mudar_tela(self, id_tela):
        ger_de_telas =self.root.ids['screen_manager'] #GERENCIADOR DE TELAS
        ger_de_telas.current = id_tela #MUDA DE TELA PELO ID

    def mudar_imagem(self,imagem):
        mudarimg = self.root.ids('screen_manager')
        mudarimg.current = imagem

#Cria um loop
DIGNUS_ESTApp().run()
