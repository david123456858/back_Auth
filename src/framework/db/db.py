from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()


DB_USERNAME = os.getenv("PGUSER")
DB_PASSWORD = os.getenv("PGPASSWORD")
DB_HOST = os.getenv("PGHOST")
DB_NAME = os.getenv("PGDATABASE")
DB_PORT = os.getenv("PGPORT", 5432)  

            
DATABASE_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=prefer"
            
             
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "keepalives": 1,
        "keepalives_idle": 30,      # Enviar keepalive cada 30 segundos de inactividad
        "keepalives_interval": 10,  # Intervalo entre keepalives después de la primera señal
        "keepalives_count": 5,       # Número de intentos antes de cerrar la conexión
    })
            
            
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

