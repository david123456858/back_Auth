from fastapi import  HTTPException,Response, status
from src.DTOS.userMorse import userMorse

class controller_morce_processing:
    def __init__(self,caseUseRegister,caseUseLoggin):
        self.caseUseRegister = caseUseRegister
        self.caseUseLoggin = caseUseLoggin
        
    async def registerCodeMorse(self,user:userMorse):
        try:
            if not user:
                return HTTPException(status_code=400,detail="faltan argumentos")
            result = await self.caseUseRegister.registerCodeMorse(user)
            return {"Data":"Se ha registrado correctamente el usuario"}
        except Exception as error:
            raise HTTPException(status_code=500,detail=f"internal error server {str(error)}")

    async def loginMorse(self,user:userMorse):
        try:
            if not user:
                return HTTPException(status_code=400,detail="faltan argumentos")
            result = await self.caseUseLoggin.loginMorse(user)
            if(result == False ):
                return HTTPException(status_code=401,detail="user or password incorrect")
            return result
        except Exception as error:
            print(error)
            raise HTTPException(status_code=500,detail=f"internal error server {str(error)}")