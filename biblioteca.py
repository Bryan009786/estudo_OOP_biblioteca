from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f"Livro com ISBN {isbn} removido.")
                return
        print(f"Nenhum livro com ISBN {isbn} encontrado.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.livros:
                print(livro)

    def buscar_por_titulo(self, palavra):
        encontrados = [livro for livro in self.livros if palavra.lower() in livro.titulo.lower()]
        if encontrados:
            for livro in encontrados:
                print(livro)
        else:
            print(f"Nenhum livro com '{palavra}' no título encontrado.")
