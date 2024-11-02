from fastapi import APIRouter, UploadFile, File
from typing import List
from src.controller.controllerFace.Face import controller_Face 
from src.config.routeConfig.routerConfig import getBaseRouter 
from pydantic import BaseModel

class RegisterFaceRequest(BaseModel):
    nameUser: str
    imagenes: List[str]

BASE_URL = getBaseRouter()
router = APIRouter()


def create_route_everything_face(controller_Face):
    @router.post(f"{BASE_URL}/registerFace", tags=['Autenticacion Facial'])
    async def register_face(request: RegisterFaceRequest):
        print("Recibiendo datos para registrar la cara.")
        try:
            nameUser = request.nameUser
            imagenes = request.imagenes
            response = await controller_Face.register_face(nameUser, imagenes)
            return nameUser
        except Exception as e:
            return {"error": str(e)}
        
        
    @router.post(f"{BASE_URL}/authFace", tags=['Autenticacion Facial'])
    async def auth_face():
        return await controller_Face.auth_face()
        
    return router
