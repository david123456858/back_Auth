import cv2
import numpy as np
from src.framework.db.db import SessionLocal
from typing import List
from fastapi import UploadFile
import base64
from sqlalchemy.orm import Session
from src.entity.User import UserFace

class caseFace_auth:
    async def decode_images(self, imgenes):
        return [
            cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
            for img in imgenes
        ]
                 
    async def auth_face(self, nameUser: str,img_reconocer_paramt: List[str]) -> dict:
        
       db: Session = SessionLocal()
       try:
           # Buscar al usuario en la tabla `users_face` según el `nameUser`
           usuario = db.query(UserFace).filter(UserFace.nameUser == nameUser).first()
           if not usuario:
               return False  # Si el usuario no existe

           imagenes_a_binaria_a_reconocer = [ base64.b64decode(img.split(',')[1]) for img in img_reconocer_paramt ]
           imagenes_entrenamiento= await self.decode_images(usuario.imagenes)
           imagen_reconocer= await self.decode_images(imagenes_a_binaria_a_reconocer)
           
           
           nombre_user = usuario.nameUser
           labels = [nombre_user] * len(imagenes_entrenamiento) 
           model = cv2.face.FisherFaceRecognizer_create()
           model.train(imagenes_entrenamiento, np.array(labels))
           prediction = model.predict(imagen_reconocer)
           
           # Calcula el porcentaje de confianza
           max_distance = 100
           confianza = max(0, (max_distance - prediction[1]) / max_distance * 100)

           if prediction[1] < 80:
               resultado =  {'autenticado':True, 'Confianza': {confianza}}  
           else:
               resultado =  {'autenticado':False, 'Confianza': {confianza}}  
           return resultado
       
       except Exception as e:
           print(f"Error al recuperar las imágenes: {e}")
           return []
       finally:
           db.close()