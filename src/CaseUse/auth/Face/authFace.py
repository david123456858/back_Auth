class caseFace_auth:
   async def auth_face():
        try:
            return " Autenticacion face"
        except Exception as e:
            print(e)
            raise Exception('Error')     

