from fastapi import APIRouter, UploadFile, File
from typing import List
from src.controller.controllerFace.Face import controller_Face 
from src.config.routeConfig.routerConfig import getBaseRouter 

BASE_URL = getBaseRouter()
router = APIRouter()

def create_route_everything_face(controller_Face):

    @router.post(f"{BASE_URL}/registerFace", tags=['Autenticacion Facial'])
    async def register_face(nombre: str, images: List[UploadFile] = File(...)):
        print("Recibiendo datos para registrar la cara.")
        try:
            response = await controller_Face.register_face(nombre, images)
            return response
        except Exception as e:
            return {"error": str(e)}
        
    @router.post(f"{BASE_URL}/authFace", tags=['Autenticacion Facial'])
    async def auth_face():
        return await controller_Face.auth_face()
        
    return router
