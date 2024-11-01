from fastapi import FastAPI, UploadFile, File, HTTPException
import json
import os
import cv2
import numpy as np
import getpass


app = FastAPI()

def cargar_configuracion():
    with open('config.json') as config_file:
        configuracion = json.load(config_file)
    return configuracion

@app.post("/registrar")
async def registrar_usuario(nombre: str, archivos: List[UploadFile] = File(...)):
    configuracion = cargar_configuracion()
    dir_faces = configuracion[getpass.getuser()]["dir_faces"]
    
    if not nombre:
        raise HTTPException(status_code=400, detail="Por favor ingrese un nombre.")
    
    path = os.path.join(dir_faces, nombre)

    if not os.path.isdir(path):
        os.mkdir(path)

    # Guardar cada archivo de imagen recibido
    for archivo in archivos:
        # Leer el contenido del archivo
        contenido = await archivo.read()
        # Guardar la imagen en el directorio correspondiente
        with open(os.path.join(path, archivo.filename), 'wb') as f:
            f.write(contenido)

    # Entrenar el modelo después de que las imágenes hayan sido guardadas
    model = cv2.face.LBPHFaceRecognizer_create()  # O el modelo que prefieras
    images, labels = [], []

    # Cargar las imágenes para entrenar
    id = 0  # Asegúrate de que este id sea único por usuario
    for (subdirs, dirs, files) in os.walk(dir_faces):
        for subdir in dirs:
            subjectpath = os.path.join(dir_faces, subdir)
            for filename in os.listdir(subjectpath):
                path = os.path.join(subjectpath, filename)
                label = id  # Cambia esto para usar un id único por usuario
                images.append(cv2.imread(path, 0))
                labels.append(int(label))
            id += 1  # Incrementa el ID para el siguiente subdirectorio

    model.train(np.array(images), np.array(labels))

    return {"message": f"Registro completado para {nombre}, imágenes recibidas: {len(archivos)}"}


@app.post("/reconocer")
async def iniciar_reconocimiento():
    configuracion = cargar_configuracion()
    dir_faces = configuracion[getpass.getuser()]["dir_faces"]

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        rval, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            face = gray[y:y + h, x:x + w]
            label, confidence = model.predict(face)
            # Aquí puedes hacer algo con el resultado del reconocimiento (label, confidence)

        # Muestra la imagen con las caras detectadas (opcional)
        cv2.imshow("Reconocimiento Facial", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return {"message": "Reconocimiento iniciado."}
