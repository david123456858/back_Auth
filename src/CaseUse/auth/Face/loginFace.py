import cv2
import numpy as np
from src.framework.db.db import SessionLocal
from typing import List
from fastapi import UploadFile
import base64
from sqlalchemy.orm import Session
from src.entity.User import UserFace


class CaseFaceRegister:
   async def register_face(self, nameUser: str, imagenes: List[str]) -> str:
       db: Session = SessionLocal()
       # Convertir las imágenes de Base64 a binario
       imagenes_binarias = [
           base64.b64decode(img.split(',')[1])  # Elimina el prefijo y convierte a bytes
           for img in imagenes
       ]
       
       try:               
           nuevo_usuario = UserFace(nameUser=nameUser, imagenes=imagenes_binarias)
           db.add(nuevo_usuario)
           db.commit() 
           db.refresh(nuevo_usuario)
               
           if (nuevo_usuario.nameUser):
               resultado =  {'Registrado':True, 'ID': {nuevo_usuario.id}} 
           else:
                resultado =  {'Registrado':False, 'ID': {nuevo_usuario.id}} 
           return resultado
       
       except Exception as e:
           print(f"Error al guardar las imágenes: {e}")
           db.rollback()  
           return "Hubo un error"
       finally:
           db.close()