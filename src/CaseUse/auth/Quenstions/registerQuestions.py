from fastapi.responses import JSONResponse
from src.DTOS.userQuestions import userQuestions

class caseUseRegisterQuestions:
    def __init__(self,repository):
        self.repository = repository
        
    async def registerQuestions(self,user:userQuestions): 
        try:
            result = self.repository.get_user_by_id(user.nameUser) 
            
            if result:
                return JSONResponse(status_code=409, content={"detail": "User already registered"})
            
            result = await self.repository.createUserQuestions(user)
            
            return {"data":"Se guardo correctamente"}
        except Exception as error:
            print(error)
            raise Exception("error in the data Base ")    