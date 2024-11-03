from fastapi.responses import JSONResponse

from src.DTOS.userQuestions import userQuestions

class caseUseLogginQuestions:
    def __init__(self,repository):
        self.repository = repository
        
    async def loginQuestions(self,user:userQuestions):
        try:    
            findUser = self.repository.get_user_by_id(user.nameUser)
            if not findUser:
                return JSONResponse(status_code=404, content={"detail": "Not found user"})
            
            for stored_question in findUser.questions:
                for key, stored_answer in stored_question.items():
                    if key in user.questions and user.questions[key] == stored_answer:
                        return {"status": "success", "message": "Question verified successfully"}
            
            return {"data":"No loggeado"}
        except Exception as e:
            raise Exception("error in the data Base ") 