from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
import bcrypt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

SECRET_KEY = "minha_chave"
ALGORITIMO = "HS256"
TEMPO_TOKEN = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verificar_senha(senha_plana: str, hash_senha: str) -> bool:
    return bcrypt.checkpw(senha_plana.encode('utf-8'), hash_senha.encode('utf-8'))

def gerar_hash_senha(senha: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')

hash_banco = gerar_hash_senha("senha123")

def criar_token_acesso(dados: dict, expires_delta: Optional[timedelta] = None):
    para_codificar = dados.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    para_codificar.update({"exp": expire})
    return jwt.encode(para_codificar, SECRET_KEY, algorithm=ALGORITIMO)

def get_usuario_atual(token: str = Depends(oauth2_scheme)):
    excecao_autenticacao = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITIMO])
        usuario: str = payload.get("sub")
        if usuario is None:
            raise excecao_autenticacao
        return usuario 
    except jwt.PyJWTError:
        raise excecao_autenticacao

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    if form_data.username != "dev" or not verificar_senha(form_data.password, hash_banco):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    access_token = criar_token_acesso(
        dados={"sub": form_data.username},
        expires_delta=timedelta(minutes=TEMPO_TOKEN)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/carteira")
def ver_carteira(usuario_logado: str = Depends(get_usuario_atual)):
    return{
        "mensagem": f"Acesso permitido para {usuario_logado}",
        "carteira": ["PETR4", "VALE3", "ITUB4"]
    }
    



