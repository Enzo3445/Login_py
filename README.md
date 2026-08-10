# 🔐 Sistema de Login e Cadastro em Python

Um sistema simples de **cadastro, login e exclusão de usuários**, desenvolvido em Python com armazenamento dos dados em um arquivo JSON.

O projeto foi criado com o objetivo de praticar conceitos fundamentais de Python, como **funções, arquivos JSON, estruturas condicionais, tratamento de exceções, loops e manipulação de dicionários**.

## 📌 Funcionalidades

O sistema possui três opções principais:

### 1. 👤 Criar conta

Permite cadastrar um novo usuário.

* Verifica se o nome de usuário já existe.
* Impede o cadastro sem nome.
* Solicita uma senha.
* Verifica se a senha é fraca através da função `detectador_de_senhafraca()`.
* Salva os dados no arquivo `usuarios.json`.

### 2. 🔑 Fazer login

Permite que um usuário entre em sua conta utilizando:

* Nome de usuário
* Senha

O sistema também registra tentativas de login incorretas e pode bloquear o usuário após atingir o limite definido.

### 3. 🗑️ Deletar conta

Permite excluir uma conta existente.

Para isso, o usuário precisa informar:

* Nome de usuário
* Senha

Após a confirmação, os dados do usuário são removidos do arquivo JSON.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **JSON**
* Manipulação de arquivos
* Funções
* Estruturas condicionais
* `match/case`
* `try/except`
* Dicionários
* Loops `while`

---

## 📂 Estrutura do projeto

```text
projeto-login/
│
├── main.py
├── funções.py
├── usuarios.json
└── README.md
```

### `main.py`

Arquivo principal responsável pelo funcionamento do sistema.

Ele controla:

* Menu principal
* Cadastro
* Login
* Exclusão de contas
* Leitura e gravação dos usuários

### `funções.py`

Contém funções utilizadas pelo programa, como:

```python
cabecalho()
detectador_de_senhafraca()
```

### `usuarios.json`

Arquivo utilizado para armazenar os usuários cadastrados.

Um exemplo da estrutura dos dados:

```json
{
    "usuario": {
        "senha": "exemplo",
        "tentativas": 0
    }
}
```

---

## ▶️ Como executar

### 1. Instale o Python

Verifique se o Python está instalado:

```bash
python --version
```

ou:

```bash
python3 --version
```

### 2. Clone o projeto

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 3. Entre na pasta

```bash
cd projeto-login
```

### 4. Execute o programa

```bash
python main.py
```

---

## 💻 Exemplo de funcionamento

Ao iniciar o programa, será apresentado um menu:

```text
Faça seu login

Digite um dos três números para o que você quer fazer

1 - criar conta
2 - para cadastrar uma conta
3 - deletar sua conta
```

O usuário poderá escolher uma das operações disponíveis.

---

## 📚 Conceitos praticados

Este projeto foi desenvolvido principalmente para praticar:

* 📦 Importação de módulos
* 🔧 Criação e utilização de funções
* 📄 Leitura de arquivos
* 💾 Persistência de dados com JSON
* 🔄 Estruturas de repetição
* 🔀 Condicionais
* 🧰 Tratamento de erros com `try/except`
* 🗃️ Manipulação de dicionários
* 🔐 Validação de senhas
* 🚫 Controle de tentativas de login

---

## ⚠️ Observação sobre segurança

Este projeto possui finalidade **educacional**.

As senhas atualmente são armazenadas diretamente no arquivo JSON, o que **não é recomendado para um sistema real**.

Em uma versão mais segura, seria interessante utilizar técnicas de **hash de senhas**, como `bcrypt` ou `Argon2`, em vez de armazenar as senhas diretamente.

---

## 🚀 Melhorias futuras

Algumas melhorias que podem ser implementadas:

* [ ] Utilizar hash de senha
* [ ] Criar sistema de logout
* [ ] Criar sessões de usuário
* [ ] Melhorar o sistema de bloqueio
* [ ] Permitir desbloqueio de contas
* [ ] Criar interface gráfica
* [ ] Migrar de JSON para SQLite
* [ ] Criar uma API com Flask ou FastAPI
* [ ] Adicionar testes automatizados
* [ ] Criar logs de eventos
* [ ] Adicionar Git e GitHub ao fluxo de desenvolvimento

---

## 🎯 Objetivo do projeto

O principal objetivo deste projeto é servir como prática de **Python e fundamentos de desenvolvimento de sistemas**, evoluindo posteriormente para conceitos de **bancos de dados, APIs e segurança da informação**.

---

## 👨‍💻 Autor

Desenvolvido como projeto de estudo em Python.

**Projeto educacional — Python + JSON + autenticação básica.**

