from src.config.routeConfig.routerConfig import getBaseRouter
from fastapi import APIRouter
from src.DTOS.userMorse import userMorse

router = APIRouter()

BASEURL = getBaseRouter()

def route_morse_everything(controller):
    
    @router.post(f"{BASEURL}/login/Morse",tags=["code-Morse"])
    async def loginMorse(user:userMorse):
        return await controller.loginMorse(user)
        
    @router.post(f"{BASEURL}/register/Morse",tags=["code-Morse"])
    async def registerMorse(user:userMorse):
        return await controller.registerCodeMorse(user)
    
    return router