from src.controller.controllerFace.Face import controller_Face 
from src.config.routeConfig.routerConfig import getBaseRouter 
from fastapi import APIRouter

BASE_URL = getBaseRouter()
router = APIRouter()


def create_route_everything_face(controller_Face):
 
    @router.post(f"{BASE_URL}/registerFace",tags=['Autenticacion Facial'])
    async def register_face():
            print("pasoooo")
            return await controller_Face.register_face()
        
    @router.post(f"{BASE_URL}/authFace",tags=['Autenticacion Facial'])
    async def auth_face():
            return await controller_Face.auth_face()
        
    return router
    
    

