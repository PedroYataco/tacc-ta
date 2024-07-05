# app/main.py

from fastapi import FastAPI,HTTPException
##from .GeneradorCuentos import generador
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from fastapi.middleware.cors import CORSMiddleware
from .generate_story import generate_story
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/generarCuento/{title}")
def read_root(title:str):
    try:
        generated_text = generate_story(prompt=title)
        return {
            "success": True,
            "data": generated_text,
            "message": f"Texto generado para el prompt: {title}"
        }
    except Exception as e:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocurrio un error al intentar generar la historia: {str(e)}"
        )
    # return {
    #     "success" : True,
    #     "data": generate_story(prompt=title),
    #     "message": "Texto generado para el prompt : " + title}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


