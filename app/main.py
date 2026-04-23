from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.database import get_db
from app.db.init_db import init_db

app =FastAPI()

# models.Base.metadata.create_all(bind=database.engine)
# Health check API ::::::
@app.get("/Health")
async def Healthcheck():
    return {"staus" : "Healthy"}

# end point to check Database is Connected or not ::::::::
@app.get("/check_database_connection")
async def check_db_connection(db:Session=Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        raise HTTPException (status_code= 500 , detail= f"database connection Failed {e}")
