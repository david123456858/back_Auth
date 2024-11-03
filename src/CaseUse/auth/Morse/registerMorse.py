from src.DTOS.userMorse import userMorse
from fastapi.responses import JSONResponse

class caseUseRegisterCodeMorse:
    def __init__(self,repository):
        self.repository = repository
    
    async def registerCodeMorse(self,user:userMorse):
        try:
            result = self.repository.get_user_by_id(user.nameUser)
            
            if result:
                return JSONResponse(status_code=409, content={"detail": "User already registered"})
            
            result = await self.repository.createUserMorse(user)
            
            return {"data":"Se guardo correctamente"}
        except Exception as e:
            
            raise Exception("error in the data Base ")            
        