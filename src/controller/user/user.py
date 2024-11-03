from fastapi import HTTPException
from fastapi.responses import JSONResponse

class controller_user:
    def __init__(self,caseUseUser):
        self.caseUseUser = caseUseUser
        
    async def getTypeAuth(self,user:str):
        try:
            if not user:
                return JSONResponse(status_code=422, content={"detail": "No se han mandado todo lo requerido"})
            
            result = self.caseUseUser.getTypeAuth(user)
            
            if not result:
                return JSONResponse(status_code=404, content={"detail": "Not Found"})
            
            return result
        except Exception as error:
            print(error)
            raise HTTPException(status_code=500,detail=f"internal error server {str(error)}") 