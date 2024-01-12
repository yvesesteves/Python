import flet as ft

def main(pagina):
    titulo = ft.Text("Hashzap")

    nome_usuario = ft.TextField(label="Escreva seu nome")
    
    chat = ft.Column()


    def enviar_mensagem_tunel(informacoes): #funçao para outras pessoas verem as mensagens
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"       # para definir quem enviou a mensagem        
        pagina.pubsub.send_all(texto_campo_mensagem)    #passar a mensagem pras pessoas q estao no chat
        campo_mensagem.value = ""       #limpar o campo mensagem
        pagina.update()


    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)     # enter ao enviar (onsubmit)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    

    def entrar_chat(evento):
        popup.open = False  #fechar o popup
        pagina.remove(botao_iniciar)    #tirar o botao 'iniciar chat' da tela
        pagina.add(chat)    # adicionar o chat
        linha_mensagem = ft.Row(    # posicionar o botao 'enviar' do lado do campo de 'enviar mensagem'
            [campo_mensagem, botao_enviar]  # criar o campo de enviar mensagem e botao de enviar
        )    
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat."
        pagina.pubsub.send_all(texto)   #mostra quem entrou no chat pora todos
        pagina.update()


    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap!"),
        content=nome_usuario,   #texto em cima da caixa
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]      #acões q o popup faz
        ) 

    def iniciar_chat(evento):   #sempre recebe um evento como parametro
        pagina.dialog = popup
        popup.open = True
        pagina.update()   #atualizar a pagina (sempre q editar uma pag dentro deu ma função, tem q dar update)
    

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat) #toda vez q clica no botao, roda a funçao
    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(main, view=ft.WEB_BROWSER)