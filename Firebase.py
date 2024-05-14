#import requests
import requests

#Importa class app
from kivy.app import App

class MyFireBase():
    API_KEY = 'AIzaSyC4Xd9rP5TpaK0E_Bnu0qBHVMqX0eGiJ_c'

    def criar_conta(self, email, senha):
        link = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}'
        print(email,senha)
        info = {'email': [email],
                'password': [senha],
                'returnSecureToken':True}
        requisicao = requests.post(link,data=info)
        requisicao_dic = requisicao.json()

        #Informa se o usuario foi criado
        if requisicao.ok:
            print('Usuário Criado com Sucesso')

            #Autenticação - ['idToken']
            id_token = requisicao_dic['idToken']

            #Token que mantem o usuário logado - ['refreshToken']
            refresh_token = requisicao_dic['refreshToken']

            #ID do Usuário - ['localId']
            local_id = requisicao_dic['localId']

            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            #Escrever em arquivo de texto
            with open ('refreshtoken.txt', 'w') as arquivo:
                arquivo.write(refresh_token)

            link = f'https://aplicativodignusest-default-rtdb.firebaseio.com/{local_id}.json'

            info_user='{"email": "email","senha": "senha"}'

            requisicao_user = requests.patch(link, data=info_user)

            meu_aplicativo.open_info_user()
            meu_aplicativo.mudar_tela('tela1')

        #exibe uma msg de erro
        else:
            msg_erro = requisicao_dic['error'] ['message']
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids['registro']
            pagina_login.ids['mensagem_login'].text = msg_erro
            pagina_login.ids['mensagem_login'].color = (1,0,0,1)
        print(requisicao_dic)




    def fazer_login(self, email, senha):
        link = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.API_KEY}'
        info = {'email': email,
                'password': senha,
                'returnSecureToken': True}
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()

        #
        if requisicao.ok:

            # Autenticação - ['idToken']
            id_token = requisicao_dic['idToken']

            # Token que mantem o usuário logado - ['refreshToken']
            refresh_token = requisicao_dic['refreshToken']

            # ID do Usuário - ['localId']
            local_id = requisicao_dic['localId']

            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            # Escrever em arquivo de texto
            with open('refreshtoken.txt', 'w') as arquivo:
                arquivo.write(refresh_token)

            meu_aplicativo.open_info_user()
            meu_aplicativo.mudar_tela('tela1')

        # exibe uma msg de erro
        else:
            msg_erro = requisicao_dic['error']['message']
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids['login']
            pagina_login.ids['mensagem_login'].text = msg_erro
            pagina_login.ids['mensagem_login'].color = (1, 0, 0, 1)
        print(requisicao_dic)

    def trocar_token(self, refresh_token):
        link = f'https://securetoken.googleapis.com/v1/token?key={self.API_KEY}'

        info = {
            "grant_type":"refresh_token",
            "refresh_token":"refresh_token"
        }
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()
        local_id = requisicao_dic('user_id')
        id_token = requisicao_dic('id_token')
        return (local_id, id_token)


