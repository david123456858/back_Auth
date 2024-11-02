from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.framework.db.db import SessionLocal,engine
from src.entity.User import Base
from src.util.verifiConnect import verifyConnectDataBase

from src.router.routerFace.Face import create_route_everything_face
from src.CaseUse.auth.Face.loginFace import CaseFaceRegister
from src.CaseUse.auth.Face.authFace import  caseFace_auth
from src.controller.controllerFace.Face import controller_Face

from src.router.auth.Morse.authMorse import route_morse_everything
from src.repository.user.userRepository import UserRepository
from src.CaseUse.auth.Morse.registerMorse import caseUseRegisterCodeMorse
from src.CaseUse.auth.Morse.loginMorse import caseUseLogginMorse
from src.controller.auth.Morse.controllerMorce import controller_morce_processing


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

dataBase = SessionLocal()
Base.metadata.create_all(bind= engine)
verifyConnectDataBase(dataBase)

#part the Code Morse
repository = UserRepository(dataBase)
caseUseRegisterMorse = caseUseRegisterCodeMorse(repository)
caseUseLogginMorse = caseUseLogginMorse(repository)
controllerMorse = controller_morce_processing(caseUseRegisterMorse,caseUseLogginMorse)
app.include_router(route_morse_everything(controllerMorse))



# part the face

caseUseRegisterFace = CaseFaceRegister(repository)
caseUseAuthFace = caseFace_auth(repository)
controllerFace = controller_Face(caseUseRegisterFace,caseUseAuthFace)
app.include_router(create_route_everything_face(controllerFace))

#Part the Questions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.framework.main:app",host="0.0.0.0",port=8000,reload=True)
