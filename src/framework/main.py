from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.framework.db.db import SessionLocal,engine
from src.entity.User import Base
from src.util.verifiConnect import verifyConnectDataBase

from src.router.routerFace.Face import create_route_everything_face
from src.CaseUse.auth.Face.loginFace import CaseFaceRegister
from src.CaseUse.auth.Face.authFace import  caseFace_auth
from src.Controller.controllerFace.Face import controller_Face

from src.router.auth.Morse.authMorse import route_morse_everything
from src.repository.user.userRepository import UserRepository
from src.CaseUse.auth.Morse.registerMorse import caseUseRegisterCodeMorse
from src.CaseUse.auth.Morse.loginMorse import caseUseLogginMorse
from src.controller.auth.Morse.controllerMorce import controller_morce_processing

from src.router.user.findTypeAuth import route_user_everything
from src.controller.user.user import controller_user
from src.CaseUse.user.userFindType import caseUseFindTypeAuth

from src.router.auth.Quentions.authQuestions import route_questions_everything
from src.controller.auth.Quenstions.controllerQuestions import controller_Questions
from src.CaseUse.auth.Quenstions.registerQuestions import caseUseRegisterQuestions
from src.CaseUse.auth.Quenstions.loginQuestions import caseUseLogginQuestions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.get('/')
def readRouteSource():
    return {"Data":"Esta subido el back"}

dataBase = SessionLocal()
Base.metadata.create_all(bind= engine)
verifyConnectDataBase(dataBase)

#part the Code Morse
repository = UserRepository(dataBase)
caseUseRegisterMorse = caseUseRegisterCodeMorse(repository)
caseUseMorseLoggin = caseUseLogginMorse(repository)
controllerMorse = controller_morce_processing(caseUseRegisterMorse,caseUseMorseLoggin)
app.include_router(route_morse_everything(controllerMorse))
  
# part the face
caseUseRegisterFace = CaseFaceRegister(repository)
caseUseAuthFace = caseFace_auth(repository)
controllerFace = controller_Face(caseUseRegisterFace,caseUseAuthFace)
app.include_router(create_route_everything_face(controllerFace))

#Part the Questions
caseUseRegisterUserQuestions = caseUseRegisterQuestions(repository)
caseUseLogginUserQuestions = caseUseLogginQuestions(repository)
controllerQuestions = controller_Questions(caseUseRegisterUserQuestions,caseUseLogginUserQuestions)
app.include_router(route_questions_everything(controllerQuestions))

#Get type auth
caseUseUserType = caseUseFindTypeAuth(repository)
controllerUserTypeAuth = controller_user(caseUseUserType)
app.include_router(route_user_everything(controllerUserTypeAuth))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.framework.main:app",host="0.0.0.0",port=8000,reload=True)