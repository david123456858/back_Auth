from src.config.routeConfig.routerConfig import getBaseRouter 

from fastapi import APIRouter

BASE_URL = getBaseRouter()

router = APIRouter()

def create_route_everything(controller):
    @router.get(f"{BASE_URL}",tags=["Base"]) #tags para la documentacion 
    async def getBase():
            print("Prueba de ruta")
            return await controller.getBase()
        
    return router   