from typing import List
from fastapi import UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from datetime import datetime

class controller_Face:
    def __init__(self, caseFace_register, caseFace_auth) -> None:
        self.caseFace_register = caseFace_register
        self.caseFace_auth = caseFace_auth        

    async def register_face(self, nombre: str, images: List[UploadFile]):
        try:
            # Verificar que se reciban los argumentos necesarios
            if not nombre or not images:
                raise HTTPException(status_code=400, detail="Faltan argumentos: nombre o imágenes")
            result = await self.caseFace_register.register_face(nombre, images)
            return result
        except Exception as error:
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(error)}")
               
    async def auth_face(self):
        try:
            # Verificar que se reciban los argumentos necesarios
            if not self.caseFace_auth:
                raise HTTPException(status_code=400, detail="Faltan argumentos")
            
            result = await self.caseFace_auth.auth_face()
            return result

        except Exception as error:
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(error)}")
