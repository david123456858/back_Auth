from fastapi.responses import JSONResponse

from src.DTOS.userQuestions import userQuestions

class caseUseLogginQuestions:
    def __init__(self,repository):
        self.repository = repository
        
    async def loginMorse(self,user:userQuestions):
        try:    
            findUser = self.repository.get_user_by_id(user.nameUser)
            if not findUser:
                return JSONResponse(status_code=404, content={"detail": "Not found user"})
            
            if (user.codeMorse != findUser.codeMorse):
                return JSONResponse(status_code=403, content={"detail": "Credentials incorrects"})
            
            return {"data":"loggeado"}
        except Exception as e:
            print(e)
            raise Exception("error in the data Base ") 