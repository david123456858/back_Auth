from src.config.routeConfig.routerConfig import getBaseRouter
from fastapi import APIRouter
from src.DTOS.userQuestions import userQuestions

router = APIRouter()

BASEURL = getBaseRouter()

def route_questions_everything(controller):
    
    @router.post(f"{BASEURL}/login/Questions",tags=["Questions"])
    async def loginQuestions(user:userQuestions):
        return await controller.loginQuestions(user)
        
    @router.post(f"{BASEURL}/register/Questions",tags=["Questions"])
    async def registerQuestions(user:userQuestions):
        return await controller.registerQuestions(user)
    
    return router