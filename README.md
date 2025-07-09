📚 estudo_OOP_biblioteca
Projeto simples em Python utilizando Programação Orientada a Objetos (POO) para simular o gerenciamento de uma biblioteca. O código está organizado em arquivos separados para melhor organização e reutilização.

✅ Objetivos
Praticar o uso de classes e objetos em Python

Separar o código em módulos (livro.py, biblioteca.py, main.py)

Implementar operações básicas: adicionar, listar, buscar e remover livros

📁 Estrutura do Projeto
bash
Copiar
Editar
estudo_OOP_biblioteca/
│
├── livro.py         # Classe Livro
├── biblioteca.py    # Classe Biblioteca
└── main.py          # Script principal com testes
🧠 Funcionalidades
Classe Livro

Atributos: título, autor, ano, ISBN

Método __str__ para exibir informações do livro de forma formatada

Classe Biblioteca

Armazena uma lista de objetos Livro

Métodos:

adicionar_livro(livro)

remover_livro(isbn)

listar_livros()

buscar_por_titulo(palavra)

🚀 Como executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu_usuario/estudo_OOP_biblioteca.git
cd estudo_OOP_biblioteca
Execute o programa principal:

bash
Copiar
Editar
python main.py
📷 Exemplo de saída
java
Copiar
Editar
--- Lista de Livros ---
O Senhor dos Anéis (1954) - J.R.R. Tolkien [ISBN: 1234567890]
Dom Quixote (1605) - Miguel de Cervantes [ISBN: 0987654321]
A Guerra dos Tronos (1996) - George R. R. Martin [ISBN: 1122334455]

--- Busca por 'Guerra' ---
A Guerra dos Tronos (1996) - George R. R. Martin [ISBN: 1122334455]

--- Remoção de Livro (ISBN: 0987654321) ---
Livro com ISBN 0987654321 removido.

--- Lista Atualizada ---
O Senhor dos Anéis (1954) - J.R.R. Tolkien [ISBN: 1234567890]
A Guerra dos Tronos (1996) - George R. R. Martin [ISBN: 1122334455]
🛠️ Requisitos
Python 3.x

📌 Autor
# Bryan Eduardo