from sqlalchemy import text

def verifyConnectDataBase(dataBase):
    try:
        result = dataBase.execute(text("SELECT 1")).fetchone()
        if result:
            print("Conexión exitosa:", result[0])  
        else:
            print("Conexión fallida")
    except Exception as e:
        print("Error en la conexión:", e)