class caseFace_register:
   async def register_face():
        try:
            return " Register Face"
        except Exception as e:
            print(e)
            raise Exception('Error')     
    