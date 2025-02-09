from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse
from app.services.bert import pregunta_respuesta  # Importa la función del modelo

# Crear la aplicación FastAPI y el router
app = FastAPI()
router = APIRouter()

@router.get("/")
async def home():
    return {"message": "¡Hola, Bounsic-back está funcionando!"}

@router.post("/ask")
async def ask(request: Request):
    data = await request.json()  # Obtener el JSON de la solicitud
    question = data.get("question", "")

    response = pregunta_respuesta(question)  # Llama a la función del modelo
    return JSONResponse(content=response)

# Incluir el router en la aplicación principal
app.include_router(router)
