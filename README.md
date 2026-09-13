# 🔒 FastAPI - Autenticação JWT & OAuth2

Uma API RESTful desenvolvida com **FastAPI** demonstrando um sistema de autenticação seguro utilizando **OAuth2** com **JWT (JSON Web Tokens)** e criptografia de senhas com **Bcrypt**.

O projeto conta com endpoints para geração de token e proteção de rotas privadas, além de ser 100% testável via a documentação automática do Swagger UI.

---

## 🚀 Funcionalidades

* **Hashing Seguro de Senhas**: Utilização do algoritmo `bcrypt` nativo para armazenar e comparar hashes de senhas.
* **Emissão de Tokens JWT**: Geração de tokens codificados em `HS256` contendo tempo de expiração (`exp`) e payload de identificação do usuário (`sub`).
* **Proteção de Rotas**: Validação automática de cabeçalhos HTTP `Authorization: Bearer <token>` através de injeção de dependências (`Depends`).
* **Documentação Interativa**: Teste completo de Login e Autorização diretamente pela interface Swagger.

---

## 🛠️ Tecnologias Utilizadas

* Python
* FastAPI
* PyJWT
* Bcrypt
* Uvicorn (Servidor ASGI)

---

## 📌 Endpoints da API

| Método | Rota | Descrição | Acesso |
| :--- | :--- | :--- | :--- |
| `POST` | `/login` | Autentica usuário e retorna o `access_token` JWT | Público |
| `GET` | `/carteira` | Retorna a carteira de investimentos do usuário | Protegido (Requer JWT) |
