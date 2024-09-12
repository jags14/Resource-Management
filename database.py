from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker

engine = create_engine('sqlite:////temp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from application import models
    Base.metadata.create_all(bind=engine)