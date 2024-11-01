from sqlalchemy.orm import Session
from src.entity.User import User  # Importa tu modelo

class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, user_data):
        new_user = User(**user_data)
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return new_user

    def get_user_by_id(self, user_id: int):
        return self.db_session.query(User).filter(User.nameUser == user_id).first()

    def update_user(self, user_id: int, updated_data):
        user = self.get_user_by_id(user_id)
        for key, value in updated_data.items():
            setattr(user, key, value)
        self.db_session.commit()
        return user

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        self.db_session.delete(user)
        self.db_session.commit()