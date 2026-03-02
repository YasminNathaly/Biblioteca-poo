class item_biblioteca: #Criei uma superclasse chamada item_biblioteca
    def __init__(self, codigo, titulo, ano):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.disponivel = True

#Adicionando métodos obrigatórios
