from sqlalchemy import Column, Integer, String, Float, DateTime
from api.config import Model

class Topic(Model):

    __tablename__ = 'topic'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, nullable=False)
    topic_id = Column('topic_id', Integer, nullable=False)

    def __init__(self, user_id: int, topic_id: int):
        self.user_id = user_id
        self.topic_id = topic_id
        