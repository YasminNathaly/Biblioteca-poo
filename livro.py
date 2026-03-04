from item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo,ano, autor, num_paginas):
        super().__init__(codigo,titulo,ano)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def exibir_detalhes(self):
        print(f"codigo: {self.get_codigo()}")
        print(f"titulo: {self.get_titulo()}")
        print(f"ano: {self.get_ano()}")
        print(f"autor: {self.get_autor()}")
        print(f"num_paginas: {self.get_num_paginas()}")
        print(f"disponivel: {self.get_disponivel()}")