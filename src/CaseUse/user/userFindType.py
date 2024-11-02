from fastapi import HTTPException

from src.util.verifyType import verifyType
class caseUseFindTypeAuth:
    def __init__(self,repository):
        self.repository = repository
        
        
    def getTypeAuth(self,user:str):
        try:
            result = self.repository.get_user_by_id(user) 
            
            resultUser = verifyType(result)
            print(result)
            
            return resultUser  
        except Exception as error:
            raise HTTPException(status_code=500,detail=f"internal error server {str(error)}")