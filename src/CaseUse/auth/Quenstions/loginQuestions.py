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
                    for question in user.questions:  # Recorrer cada pregunta en la lista de preguntas de la solicitud
                        if key in question and question[key] == stored_answer:
                            return {"status": "success", "message": "Question verified successfully"}
            
            return JSONResponse(status_code=403, content={"detail": "Credentials incorrects"})
        except Exception as e:
            print(e)
            raise Exception("error in the data Base ") 