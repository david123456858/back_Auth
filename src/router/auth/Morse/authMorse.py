from src.config.routeConfig.routerConfig import getBaseRouter
from fastapi import APIRouter


router = APIRouter()

BASEURL = getBaseRouter()

def route_morse_everything(controller):
    @router.post(f"{BASEURL}/login/Morse",tags=["code-Morse"])
    async def loginMorse():
        print(2)
        
    @router.post(f"{BASEURL}/register/Morse",tags=["code-Morse"])
    async def registerMorse():
        print(2)