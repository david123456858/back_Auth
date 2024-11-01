from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class DB:
    _instance = None  
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
        
            DB_USERNAME = os.getenv("PGUSER")
            DB_PASSWORD = os.getenv("PGPASSWORD")
            DB_HOST = os.getenv("PGHOST")
            DB_NAME = os.getenv("PGDATABASE")
            DB_PORT = os.getenv("PGPORT", 5432)  

            
            cls.DATABASE_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            
            
            cls._instance.engine = create_engine(cls.DATABASE_URL)
            
            
            cls._instance.SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=cls._instance.engine)
        
        return cls._instance
    
    def get_session(self):
        
        return self.SessionLocal()
