# 📒 Agenda de Contatos

Projeto em Python que simula uma agenda de contatos interativa via terminal, com funcionalidades de adicionar, buscar e listar contatos, incluindo tratamento de duplicatas e validação de entradas.

---

# Descrição

O programa oferece um menu interativo onde o usuário pode gerenciar seus contatos, armazenando nome, telefone e e-mail. A agenda detecta contatos duplicados e pergunta se o usuário deseja substituí-los, além de oferecer a opção de cadastrar um novo contato diretamente ao fazer uma busca sem resultado.

---

# Funcionalidades

- **Adicionar contato:** cadastra nome, telefone e e-mail
- **Buscar contato:** localiza um contato pelo nome e exibe seus dados
- **Listar contatos:** exibe todos os contatos salvos na agenda
- **Sair:** encerra o programa
- Detecção de duplicatas com opção de substituição
- Cadastro rápido ao buscar um contato inexistente
- Validação de todas as entradas do usuário

---

# Como executar

**Pré-requisito:** Python 3.x instalado.

```bash
python agenda.py
```

---

# Exemplo de uso

```
---AGENDA---

Escolha um número:
1. Adicionar
2. Buscar
3. Listar
4. Sair
1

Digite o nome: samuel
Digite o telefone: 41999990000
Digite o email: samuel@email.com

Escolha um número:
1. Adicionar
2. Buscar
3. Listar
4. Sair
3

samuel -> 41999990000 | samuel@email.com
```

---

# Conceitos praticados

- Dicionários aninhados (`dict` dentro de `dict`) para estruturar os contatos
- Laço `while True` com `break` para controle do menu
- Método `.get()` para verificação segura de chaves no dicionário
- Validação de entrada com laços `while` aninhados
- Iteração com `.items()` para listagem de contatos
- Uso de `continue` para retornar ao menu sem executar o restante do bloco
- Formatação de strings com f-strings

---

# 👤 Autor

**Samuel Archila**  
Estudante de Data Science | Python | SQL | Power BI  
[LinkedIn](https://www.linkedin.com/in/samuelarchila)
