from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controller.baseController.baseController import controller_processing
from src.router.routerBase.routeBase import create_route_everything
from src.framework.db.db import SessionLocal,engine
from src.entity.User import Base
from src.util.verifiConnect import verifyConnectDataBase

from src.router.routerFace.Face import create_route_everything_face
from src.caseUse.auth.Face.loginFace import caseFace_register
from src.caseUse.auth.Face.authFace import  caseFace_auth
from src.controller.controllerFace.Face import controller_Face




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
    
controllerBase = controller_processing()
app.include_router(create_route_everything(controllerBase)) #Enrutador

# part the face
caseUseRegisterFace = caseFace_register()
caseUseAuthFace = caseFace_auth()
controllerFace = controller_Face(caseUseRegisterFace,caseUseAuthFace)
app.include_router(create_route_everything_face(controllerFace))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.framework.main:app",host="0.0.0.0",port=8000,reload=True)
