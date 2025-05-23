from fastapi import HTTPException
from fastapi.responses import JSONResponse

from src.util.verifyType import verifyType
class caseUseFindTypeAuth:
    def __init__(self,repository):
        self.repository = repository
        
        
    def getTypeAuth(self,user:str):
        try:
            result = self.repository.get_user_by_id(user) 
            
            if not result:
                return JSONResponse(status_code=404, content={"detail": "Not found user"})
            
            resultUser = verifyType(result)
            res = {
                "userInfo":resultUser.__dict__ 
            }
            if resultUser.typeAuth == "Questions":
                res["questions"] = result.questions
                
            return JSONResponse(content=res)
        except Exception as error:
            raise HTTPException(status_code=500,detail=f"internal error server {str(error)}")