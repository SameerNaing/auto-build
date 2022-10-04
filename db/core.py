from sqlalchemy.orm import Session
from contextlib import contextmanager

from system.decorators import change_autobuild_dir
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


@contextmanager
@change_autobuild_dir
def get_session() -> Session:
    engine = create_engine("sqlite:///db/autobuild.db")
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session = Session()
    try:
        yield session
    finally:
        Session.remove()
