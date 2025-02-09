from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn
from routes import bert_router 
from routes.ri import router as rutas1_router

if not load_dotenv('env/.env.dev'):
    print("⚠️ No se pudo cargar el archivo .env.dev")

# Inicializar FastAPI
app = FastAPI()

# Leer las variables de entorno
env_host = os.getenv("HOST", "localhost")
env_mode = os.getenv("FLASK_ENV", "production")  # No se usa en FastAPI, pero puede ser útil
app_port = int(os.getenv("APP_PORT", 5000))
debug_mode = os.getenv("DEBUG", "False") == "True"
secret_key = os.getenv("SECRET_KEY", "defaultsecret")
print(f"HOST: {env_host}, PORT: {app_port}, DEBUG: {debug_mode}")


# Registrar routers (equivalente a Blueprints en Flask)
app.include_router(bert_router, prefix="/bert")
app.include_router(rutas1_router, prefix="/rutas1")

# Ruta principal
@app.get("/")
async def home():
    return {"message": "¡Bienvenido a FastAPI en Bounsic-back!"}

if __name__ == "__main__":
    print(f"🚀 Servidor corriendo en: http://{env_host}:{app_port} (modo: {env_mode})")
    uvicorn.run(
        "app.server:app",  # Cambia "main:app" por "app.server:app"
        host=env_host,
        port=app_port,
        reload=debug_mode
    )



