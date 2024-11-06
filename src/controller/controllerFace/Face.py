from fastapi import HTTPException
from fastapi.responses import JSONResponse

from src.DTOS.userFace import userFace


class controller_Face:
    def __init__(self, caseFace_register, caseFace_auth) -> None:
        self.caseFace_register = caseFace_register
        self.caseFace_auth = caseFace_auth        

    async def register_face(self, user:userFace)-> dict:
        nameUser = user.nameUser
        imagenes = user.imagenes
        
        print(len(imagenes))
        if not nameUser or not isinstance(imagenes, list) or len(imagenes) != 100:
            return JSONResponse(status_code=422, content={"detail": "No se han mandado todo lo requerido"}) 
        try:
            result = await self.caseFace_register.register_face(user)
            return result
        except Exception as error:
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(error)}")
        
    
    async def auth_face(self, user: userFace) -> dict:
        nameUser = user.nameUser
        imagenes = user.imagenes
        
        if not nameUser or not isinstance(imagenes, list) or len(imagenes) != 1:
            return JSONResponse(status_code=422, content={"detail": "No se han mandado todo lo requerido"})
        try:
            result = await self.caseFace_auth.auth_face(user)
            return result
        except Exception as e:
            print(f"Error durante la autenticación: {e}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")