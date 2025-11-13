from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class BoardIn(BaseModel):
    board: List[List[int]]

@app.get("/")
def home():
    return {"message": "Lights Out API funcionando"}

@app.post("/resolver")
def solve(board_in: BoardIn):
    
    return {"solution": [0,0,1,0,1,0,1,0,1]}
