from src.DTOS.userMorse import userMorse
from fastapi import HTTPException,Response,status

class caseUseLogginMorse:
    def __init__(self,repository):
        self.repository = repository
        
    async def loginMorse(self,user:userMorse):
        try:
            findUser = self.repository.get_user_by_id(user.nameUser)
            if not findUser:
                return HTTPException(status_code=404,detail="user not found")
            
            if (user.codeMorse != findUser.codeMorse):
                return False
            
            return {"data":"loggeado"}
        except Exception as e:
            print(e)
            raise Exception("error in the data Base ") 