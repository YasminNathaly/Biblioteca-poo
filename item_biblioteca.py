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
    


    