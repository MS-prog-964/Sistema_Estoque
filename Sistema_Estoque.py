class Login:
    def __init__(self):
        self.usuario = ""
        self.senha = ""
    def Cadastro_usuario(self):
        self.usuario = input("Cadastro de usuário: ")
        self.senha = input("Cadastre a senha: ")
        print(f"\n Usuário Cadastrado: {self.usuario}")
        print(f"\n senha cadastrada: {self.senha}")
        print("Usuário Cadastrado com sucesso!")
    def verificacao_cadastro(self, usuario_cadastrado, senha_acesso):
        if usuario_cadastrado == self.usuario and senha_acesso == self.senha:
            print("Usuário verificado, Bem vindo!")
            return True
        else:    
            print("Usuário ou senha incorreta! Verifique as informações digitadas")
            return False
class Produto:
    def __init__(self):
        self.nome_produto = ""
        self.qtd_produto = 0
        self.lista_produto = []
    def vender_produto(self):    
        self.nome_produto = input("Produto a venda: ")
        self.qtd_produto = int(input("Quantidade de produtos: "))
        for item in self.lista_produto:
            if item['nome'].lower()== self.nome_produto.lower():
             if item['qtd'] >= self.qtd_produto:
                item['qtd']-=self.qtd_produto
                print(f"Venda realizada, faltam {item['qtd']} unidades disponíveis")
             else:
                print("Produto indisponível")
                return
        else:   
            print("Produto inexistente") 
        while True:
         print("\n === MENU PRINCIPAL ===")
         print("1 - Vender Produto")
         print("2 - Sair")
         
         opcao = input("Escolha uma opção: ")
         
         if opcao == "1":
             produto.vender_produto()
         elif opcao == "2":
             print("Saindo do sistema...")
             break
         else:
             print("Opção inválida!")
usuario = Login()
usuario.Cadastro_usuario()
usuario_cadastrado = input("Digite seu usuário: ")
senha_acesso= input("Digite sua senha: ")
if usuario.verificacao_cadastro(usuario_cadastrado, senha_acesso):  
    produto = Produto()
    
    while True:
        print("\n---Menu Principal---")  
        print("\n 1 - Vender Produtos: ")
        print("\n 2 - Sair: ")
        
        opcao = input("Escolha o produto: ")
        if  opcao == "1":
         produto.vender_produto()
        elif  opcao == "2":
         print("Produto removido do sistema")
         break
        else:
         print("Escolha inválida")
          
        