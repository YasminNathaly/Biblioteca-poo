from item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, edicao, mes):
        super().__init__(codigo, titulo, ano)
        self.__edicao = edicao
        self.__mes = mes

    def exibir_detalhes(self):
        print(f"codigo: {self.get_codigo()}")
        print(f"titulo: {self.get_titulo()}")
        print(f"ano: {self.get_ano()}")
        print(f"edicao: {self.get_edicao()}")
        print(f"mes: {self.get_mes()}")
        print(f"disponivel: {self.get_disponivel()}")