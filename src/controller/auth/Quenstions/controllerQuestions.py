from fastapi import HTTPException
from fastapi.responses import JSONResponse

from src.DTOS.userQuestions import userQuestions

class controller_Questions:
    def __init__(self,caseUseRegister,caseUseLoggin):
        self.caseUseRegister=caseUseRegister
        self.caseUseLoggin=caseUseLoggin
     
    async def registerQuestions(self,user:userQuestions):
        try:
            if not user:
                return JSONResponse(status_code=422, content={"detail": "No se han mandado todo lo requerido"})
            
            
            result = await self.caseUseRegister.registerQuestions(user)
            
            return {"Data":"Se ha registrado correctamente el usuario"}
        
        except Exception as error:
            
            raise HTTPException(status_code=500,detail=f"internal error server {str(error)}")
        