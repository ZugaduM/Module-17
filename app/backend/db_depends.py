from .db import local_session

async def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()