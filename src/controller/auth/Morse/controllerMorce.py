from fastapi import  HTTPException

class controller_morce_processing:
    def __init__(self,caseUseRegister,caseUseLoggin):
        self.caseUseRegister = caseUseRegister
        self.caseUseLoggin = caseUseLoggin
        
    async def registerCodeMorse():
        try:
            print("Entre al controllador")
            
        except Exception as error:
            raise HTTPException(status_code=500,detail=f"internal error server {str(error)}")
          