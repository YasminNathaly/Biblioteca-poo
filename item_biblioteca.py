class item_biblioteca: #Criei uma superclasse chamada item_biblioteca
    def __init__(self, codigo, titulo, ano, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.disponivel = True

#Adicionando métodos obrigatórios
    def get_codigo(self):
        return self.__codigo
    def get_titulo(self):
        return self.__titulo
    def get_ano(self):
        return self.__ano
    def get_disponivel(self):
        return self.__disponivel
    
#Validando
    def set_titulo(self,titulo):
        if titulo.strip():
            self.__titulo = titulo
        else:
            print("Titulo inválido.")

    def set_ano(self, ano):
        if ano > 0:
            self.__ano = ano
        else:
            print("Ano inválido.")

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Item '{self.__titulo}' emprestado com sucesso.")
        else:
            print(f"Item '{self.__titulo}' já está emprestado.")

    def devolver(self):
        self.__disponivel = True
        print(f"Item '{self.__titulo}' devolvido com sucesso.")

    def exibir_detalhes(self):
        pass