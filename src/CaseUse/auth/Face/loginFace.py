import base64
from src.DTOS.userFace import userFace

class CaseFaceRegister:
    def __init__(self,repository):
        self.repository = repository
        
    async def register_face(self, user:userFace) -> dir:
    
       # Convertir las imágenes de Base64 a binario
       imagenes_binarias = [
           base64.b64decode(img.split(',')[1])  # Elimina el prefijo y convierte a bytes
           for img in  user.imagenes
       ]
       
       try:               
         #  nuevo_usuario = UserFace(nameUser=user.nameUser, imagenes=imagenes_binarias)
           user.imagenes = imagenes_binarias    
           result = await self.repository.createUserFase(user)
           if (result):
               resultado =  {'Registrado':True} 
           else:
                resultado =  {'Registrado':False} 
           return resultado
       
       except Exception as e:
           print(f"Error al guardar las imágenes: {e}")
           return "Hubo un error"