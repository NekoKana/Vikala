import os
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
  **{
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'hoge'),
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'database': os.getenv('DB_DATABASE', 'huga')
  })

SQLALCHEMY_ECHO = False

ENGINE = create_engine(
    SQLALCHEMY_DATABASE_URI,
    encoding="utf-8",
    pool_recycle=2500,
    echo=SQLALCHEMY_ECHO
)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

Model = declarative_base()
Model.query = session.query_property()
