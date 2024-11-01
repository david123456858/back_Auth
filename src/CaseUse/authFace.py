from fastapi import FastAPI, UploadFile, File, HTTPException
import json
import os
import cv2
import numpy as np
from datetime import datetime
import getpass

app = FastAPI()

def cargar_configuracion():
    with open('config.json') as config_file:
        configuracion = json.load(config_file)
    return configuracion

@app.post("/entrenar")
async def iniciar_entrenamiento(nombre: str):
    configuracion = cargar_configuracion()
    dir_faces = configuracion[getpass.getuser()]["dir_faces"]
    
    if not nombre:
        raise HTTPException(status_code=400, detail="Por favor ingrese un nombre.")
    
    path = os.path.join(dir_faces, nombre)
    size = 4

    if not os.path.isdir(path):
        os.mkdir(path)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    img_width, img_height = 112, 92
    count = 0

    # Aquí se tendría que realizar un bucle para capturar imágenes (esto sería mejor manejarlo en un hilo separado o de otra manera no bloqueante)
    while count < 100:
        rval, img = cap.read()
        img = cv2.flip(img, 1, 0)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

        faces = face_cascade.detectMultiScale(mini)
        faces = sorted(faces, key=lambda x: x[3])
    
        if faces:
            face_i = faces[0]
            (x, y, w, h) = [v * size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (img_width, img_height))
        
            pin = sorted([int(n[:n.find('.')]) for n in os.listdir(path) if n[0] != '.'] + [0])[-1] + 1
            cv2.imwrite('%s/%s.png' % (path, pin), face_resize)

            count += 1

    cap.release()
    cv2.destroyAllWindows()

    return {"message": f"Entrenamiento completado para {nombre}, imágenes capturadas: {count}"}










@app.post("/reconocer")
async def iniciar_reconocimiento(metodo_seleccionado: int):
    configuracion = cargar_configuracion()
    dir_faces = configuracion[getpass.getuser()]["dir_faces"]
    
    if metodo_seleccionado not in [1, 2, 3]:
        raise HTTPException(status_code=400, detail="Por favor seleccione un tipo de algoritmo de reconocimiento válido.")
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    (images, labels, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(dir_faces):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(dir_faces, subdir)
            for filename in os.listdir(subjectpath):
                path = os.path.join(subjectpath, filename)
                label = id
                images.append(cv2.imread(path, 0))
                labels.append(int(label))
            id += 1

    images = np.array(images)
    labels = np.array(labels)

    if metodo_seleccionado == 1:
        model = cv2.face.EigenFaceRecognizer_create()
    elif metodo_seleccionado == 2:
        model = cv2.face.FisherFaceRecognizer_create()
    elif metodo_seleccionado == 3:
        model = cv2.face.LBPHFaceRecognizer_create()

    model.train(images, labels)

    # Aquí deberías agregar la lógica para el reconocimiento facial con la cámara, similar a la lógica de tu función
    # en el método iniciar_reconocimiento(). Sin embargo, ten en cuenta que este código es sin bloqueo y
    # puede ser complicado manejar en un entorno de backend.

    cap.release()
    cv2.destroyAllWindows()

    return {"message": "Reconocimiento iniciado."}

@app.get("/")
async def root():
    return {"message": "API de Reconocimiento Facial en funcionamiento."}
