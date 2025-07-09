from livro import Livro
from biblioteca import Biblioteca

# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "1234567890")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "0987654321")
livro3 = Livro("A Guerra dos Tronos", "George R. R. Martin", 1996, "1122334455")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando todos os livros
print("\n--- Lista de Livros ---")
biblioteca.listar_livros()

# Buscando por título
print("\n--- Busca por 'Guerra' ---")
biblioteca.buscar_por_titulo("Guerra")

# Removendo um livro
print("\n--- Remoção de Livro (ISBN: 0987654321) ---")
biblioteca.remover_livro("0987654321")

# Listando novamente
print("\n--- Lista Atualizada ---")
biblioteca.listar_livros()
