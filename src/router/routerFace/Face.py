from fastapi import APIRouter, UploadFile, File
from typing import List
from src.controller.controllerFace.Face import controller_Face 
from src.config.routeConfig.routerConfig import getBaseRouter 
from pydantic import BaseModel
from src.DTOS.userFace import userFace

BASE_URL = getBaseRouter()
router = APIRouter()


def create_route_everything_face(controller_Face):
    @router.post(f"{BASE_URL}/registerFace", tags=['Autenticacion Facial'])
    async def register_face(user: userFace)-> dict:
        try:
            print("Entro")
            response = await controller_Face.register_face(user)
            return response
        except Exception as e:
            return {"error": str(e)}
        
        
    @router.post(f"{BASE_URL}/authFace", tags=['Autenticacion Facial'])
    async def auth_face(user: userFace) -> dict:
        try:
            print("entro al aut face")
            response = await controller_Face.auth_face(user)
            return response
        except Exception as e:
            return {"error": str(e)}
        
    return router
