from fastapi import APIRouter

from src.config.routeConfig.routerConfig import getBaseRouter

router = APIRouter()

BASEURL = getBaseRouter()

def route_user_everything(controller):
    
    @router.get(f"{BASEURL}/type/{{user}}",tags=["user"])
    async def getTypeAuth(user:str):
        return await controller.getTypeAuth(user)
        
    return router