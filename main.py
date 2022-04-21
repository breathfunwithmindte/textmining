# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from src.TextMining import TextMining
from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.mount("/static", StaticFiles(directory="./static"), name="static")

@app.get("/")
def homepage ():
    return { "hello": "world" }

def run():
    schema = {
        "simulateAI": [
            { "name": "felling happy", "keywords": ["wow", "awesome"] },
            { "name": "felling sad", "keywords": ["its bad", "no way"] }
        ]
    }

    textmining = TextMining("wow")
    textmining.hello()
      # Press Ctrl+F8 to toggle the breakpoint.


# if __name__ == '__main__':
#     run()
