import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import tekore as tk
from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI  
import uvicorn
from typing import Optional
from pydantic import BaseModel
import basilica
from model import Record, create_table, drop_table
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from spotify import audio_features, album_songs
from schemas import Record



client_id = os.getenv("CLIENT_ID")
client_secret_id = os.getenv("CLIENT_SECRET_ID")
basilica_key = os.getenv("BASILICA_KEY")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret_id)
BASILICA = basilica.Connection(basilica_key)

app_token = tk.request_client_token(client_id, client_secret_id)
sp = tk.Spotify(app_token)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
@app.get("/Home")
def get_home():
    return {"Hello": "World"}

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
    all_cats = sp.categories(limit=50)
    for cat in all_cats.items:
        print(cat.name)
        return
@app.get("/albums")
def album_songs():
    return album_songs()
    
@app.get("/Audio")
def audio_features():
    print(audio_features())
    return 

@app.post("/Reset")
def reset():
    drop_table()
    create_table()
    return
    



    

