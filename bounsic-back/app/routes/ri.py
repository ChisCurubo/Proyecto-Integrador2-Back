from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {"message": "¡Bienvenido a la sección de /rutas1!"}

@router.get("/about")
async def about():
    return {"message": "Acerca de la segunda colección de rutas"}
