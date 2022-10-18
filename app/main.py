from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from . import mymodels
from .dbase import  SQLALCHEMY_DATABASE_URL, engine
from .routers import mypost, myusers, auth_login, mylikes
from .config import settings

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mypost.router)
app.include_router(myusers.router)
app.include_router(auth_login.router)
app.include_router(mylikes.router)

app.config[SQLALCHEMY_DATABASE_URL] = 'postgres://vysqnvfobmvmri:55c2ee0a2a3dfb898b892f555bddd036145395e3a88dcf9a842737873bbd8840@ec2-52-70-45-163.compute-1.amazonaws.com:5432/deir032mr792t2'

@app.get('/')
def root():
    return {"message":"i will build something better !"} 

