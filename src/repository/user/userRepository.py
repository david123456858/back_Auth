from sqlalchemy.orm import Session

from src.entity.User import User  # Importa tu modelo
from src.DTOS.userMorse import userMorse
from src.DTOS.userFace import userFace
from src.DTOS.userQuestions import userQuestions


class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    
    async def createUserMorse(self,user:userMorse):
        new_user = User(**user.__dict__)
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return new_user
    
    async def createUserQuestions(self,user:userQuestions):
        new_user = User(**user.__dict__)
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return new_user
    
    async def createUserFase(self,user:userFace):
        new_user = User(**user.__dict__)
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return new_user
    
    def get_user_by_id(self, user_id: str):
        return self.db_session.query(User).filter(User.nameUser == user_id).first()
    
    
    def get_user_by_name(self, nameUser: str):
        return self.db_session.query(User).filter(User.nameUser == nameUser).first()


    def update_user(self, user_id: str, updated_data):
        user = self.get_user_by_id(user_id)
        for key, value in updated_data.items():
            setattr(user, key, value)
        self.db_session.commit()
        return user
    
    def delete_user(self, user_id: str):
        user = self.get_user_by_id(user_id)
        self.db_session.delete(user)
        self.db_session.commit()