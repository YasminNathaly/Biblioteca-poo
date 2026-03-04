class Biblioteca:
    def __init__(self):
        self.__itens =[]

    def adicionar_item(self, item):
        self.__itens.append(item)
        print(f"item: '{item.get_titulo()}'Adicionado com sucesso!")

    def listar_itens(self):
        if not self.__itens:
            print("Nenhum item cadastrado.")
        else:
            for item in self.__itens:
                item.exibir_detalhes()

    def buscar_item_por_codigo(self, codigo):
        item = self.buscar_item_por_codigo(codigo)
        for item in self.__itens:
            if item.get_codigo() == codigo:
                return item
            return None
        
    def  emprestar_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.emprestar()
        else:
            print(f"item com codigo{codigo} não encontrado.")

    def devolver_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.devolver()
        else:
            print(f"Item com codigo{codigo}não encontrado.")