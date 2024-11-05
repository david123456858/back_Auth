import base64
from src.DTOS.userFace import userFace
from src.CaseUse.auth.Face.authFace import caseFace_auth

class CaseFaceRegister:
    def __init__(self,repository):
        self.repository = repository
        
    async def register_face(self, user:userFace) -> dict: 
        usuario = self.repository.get_user_by_name(user.nameUser) 
        if (usuario):             
                return {'Registrado':False, 'Mensaje':"Ya existe un lote de imagenes para ese nombre de usuario"} 
            
        try:
            imagenes_binarias = await caseFace_auth.decodificar_imagenes_base64(self,user.imagenes)
            user.imagenes = imagenes_binarias    
            result = await self.repository.createUserFase(user)
            if (result):
                resultado =  {'Registrado':True, 'Mensaje':'Galeria generada'} 
            else:
                resultado =  {'Registrado':False, 'Mensaje':'No se registraron las imagenes'} 
            return resultado
        
        except Exception as e:
            print(f"Error al guardar las imágenes: {e}")
            return "Hubo un error"