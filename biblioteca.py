class Biblioteca:
    def __init__(self):
        self.__itens =[]

    def adicionar_item(self, item):
        self.__itens.append(item)
        print(f"item: '{item.get_titulo()}'Adicionado com sucesso!")

        