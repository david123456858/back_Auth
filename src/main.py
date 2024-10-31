from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controller.baseController.baseController import controller_processing
from src.router.routerBase.routeBase import create_route_everything

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

controllerBase = controller_processing()

app.include_router(create_route_everything(controllerBase))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app",host="0.0.0.0",port=8000,reload=True)
