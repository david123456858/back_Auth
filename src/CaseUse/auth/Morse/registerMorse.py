from src.DTOS.userMorse import userMorse
from fastapi import HTTPException
class caseUseRegisterCodeMorse:
    def __init__(self,repository):
        self.repository = repository
    
    async def registerCodeMorse(self,user:userMorse):
        try:
            print(user)
            findUser = self.repository.get_user_by_id(user.nameUser)
            
            if(findUser):
                return HTTPException(status_code=404,detail="user ya existente")
            
            result = await self.repository.createUserMorse(user)
            print(result)
            return result
        except Exception as e:
            print(e)
            raise Exception("error in the data Base ")            
        