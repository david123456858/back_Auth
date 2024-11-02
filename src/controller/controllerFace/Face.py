from typing import List
from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from datetime import datetime
from src.DTOS.userFace import userFace


class controller_Face:
    def __init__(self, caseFace_register, caseFace_auth) -> None:
        self.caseFace_register = caseFace_register
        self.caseFace_auth = caseFace_auth        

    async def register_face(self, user:userFace):
        try:
            # Verificar que se reciban los argumentos necesarios
            nameUser = user.nameUser
            imagenes = user.imagenes
            if not nameUser or not imagenes:
                raise HTTPException(status_code=400, detail="Faltan argumentos")
            result = await self.caseFace_register.register_face(user)
            return result
        except Exception as error:
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(error)}")
         
    async def auth_face(self, user:userFace):
        try:
            # Verificar que se reciban los argumentos necesarios
            nameUser = user.nameUser
            imagenes = user.imagenes
            if not nameUser or not imagenes:
                raise HTTPException(status_code=400, detail="Faltan argumentos")
            result = await self.caseFace_auth.auth_face(user)
            return result
        except Exception as error:
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(error)}")