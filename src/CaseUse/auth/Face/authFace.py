import cv2
import numpy as np
import base64
from src.entity.User import UserFace
from src.DTOS.userFace import userFace

class caseFace_auth:
    def __init__(self, repository):
        self.repository = repository

    async def decode_images_cv(self, imgenes):
        return [
            cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
            for img in imgenes
        ]
        
    async def decodificar_imagenes_base64(self, imgenes):
        return [base64.b64decode(img.split(',')[1]) for img in  imgenes]


    async def escala_grises(self, imgenes):
        return [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in imgenes]
    
    
    async def auth_face(self, user: userFace) -> dict:
        usuario = self.repository.get_user_by_name(user.nameUser)
        if not usuario:
            return {'autenticado': False, 'Mensaje': "No existe"}
        try:
            # Decodificar imágenes de entrada
            imagenes_a_binaria_a_reconocer = await self.decodificar_imagenes_base64(user.imagenes) 
            imagenes_entrenamiento = await self.decode_images_cv(usuario.imagenes)

            # Convertir imágenes de entrenamiento a escala de grises
            imagenes_entrenamiento_grises = await self.escala_grises(imagenes_entrenamiento)
            imagenes_reconocer_grises = await self.escala_grises(await self.decode_images_cv(imagenes_a_binaria_a_reconocer))
                        
            # Etiquetas para el entrenamiento (en este caso, solo una etiqueta por usuario)
            labels = np.zeros(len(imagenes_entrenamiento_grises), dtype=np.int32)

            # Crear el modelo y entrenarlo
            model = cv2.face.LBPHFaceRecognizer_create()
            model.train(imagenes_entrenamiento_grises, labels)

            # Realizar las predicciones
            resultados = []
            for img in imagenes_reconocer_grises:
                label, confidence = model.predict(img)
                confianza = max(0, (100 - confidence) / 100 * 100)  # Calcula el porcentaje de confianza
                resultados.append({'label': label, 'confidence': confianza})
            # Verifica si la confianza es suficiente para autenticar
            if any(r['confidence'] >= 80 for r in resultados):  # Cambia 80 al umbral que prefieras
                return {'autenticado': True, 'confianza':resultados[0]['confidence']}
            else:
                return {'autenticado': False, 'confianza': resultados[0]['confidence']}
            
        except Exception as e:
            print(f"Error al recuperar las imágenes: {e}")
            return {'autenticado': False, 'Mensaje': str(e)}
