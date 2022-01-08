from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class Topic(Model):

    __tablename__ = 'topic'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('topic_id', Integer, nullable=False)
    topic_name = Column('topic_name', String(50), nullable=False)

    def __init__(self, user_id: int, natopic_nameme: str):
        self.user_id = user_id
        self.topic_name = topic_name
