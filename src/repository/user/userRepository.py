from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from src.entity.User import User  # Importa tu modelo
from src.DTOS.userMorse import userMorse
from src.DTOS.userFace import userFace
from src.DTOS.userQuestions import userQuestions


class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    
    async def createUserMorse(self,user:userMorse):
        try:
            new_user = User(**user.__dict__)
            self.db_session.add(new_user)
            self.db_session.commit()
            self.db_session.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            self.db_session.rollback()
        finally :
            self.db_session.close()
    
    async def createUserQuestions(self,user:userQuestions):
        try:
            new_user = User(**user.__dict__)
            self.db_session.add(new_user)
            self.db_session.commit()
            self.db_session.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            self.db_session.rollback()
        finally :
            self.db_session.close()
    
    async def createUserFase(self,user:userFace):
        try:
            new_user = User(**user.__dict__)
            self.db_session.add(new_user)
            self.db_session.commit()
            self.db_session.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            self.db_session.rollback()
        finally :
            self.db_session.close()
    
    def get_user_by_id(self, user_id: str):
        try:
            return self.db_session.query(User).filter(User.nameUser == user_id).first()
        except SQLAlchemyError as e: 
            self.db_session.rollback()
        finally:
            self.db_session.close()    
    