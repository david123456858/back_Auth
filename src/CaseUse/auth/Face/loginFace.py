from src.DTOS.userFace import userFace
from src.CaseUse.auth.Face.authFace import caseFace_auth

from fastapi.responses import JSONResponse

class CaseFaceRegister:
    def __init__(self,repository):
        self.repository = repository
        
    async def register_face(self, user:userFace): 
        usuario = self.repository.get_user_by_id(user.nameUser) 
        if (usuario):             
                return {'Registrado':False, 'Mensaje':"Ya existe un lote de imagenes para ese nombre de usuario"} 
            
        try:
            imagenes_binarias = await caseFace_auth.decodificar_imagenes_base64(self,user.imagenes)
            user.imagenes = imagenes_binarias    
            result = await self.repository.createUserFase(user)
            if (result):
                print("Entro En register case use")
                return JSONResponse(status_code=200, content={'Registrado':True, 'Mensaje':'Galeria generada'})
            else:
                return JSONResponse(status_code=500, content={'Registrado':False, 'Mensaje':'No se registraron las imagenes'} )
        
        except Exception as e:
            print(f"Error al guardar las imágenes: {e}")
            return "Hubo un error"