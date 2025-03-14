from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from pydantic import BaseModel
from gemini_utility import (
    gemini_pro_response,
    gemini_pro_vision_response,
    embeddings_model_response,
    gemini_pro_sport_response,
)
from PIL import Image
import io
import json
import datetime
import requests

app = FastAPI()


class EmbedRequest(BaseModel):
    text: str


class AskRequest(BaseModel):
    question: str


class SportRequest(BaseModel):
    sport_query: str


@app.post("/image-insight")
async def image_insight(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    caption = gemini_pro_vision_response("Describe this image in a few words.", image)
    return {"caption": caption}


@app.post("/embed-text")
async def embed_text(request: EmbedRequest):
    try:
        response = embeddings_model_response(request.text)
        return {"embeddings": response}
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=422, detail=f"JSON decode error: {str(e)}")


@app.post("/ask-anything")
async def ask_anything(request: AskRequest):
    response = gemini_pro_response(request.question)
    return {"response": response}


@app.get("/current-datetime")
async def get_current_datetime():
    current_datetime = datetime.datetime.now()
    return {"current_datetime": current_datetime.isoformat()}


@app.get("/location")
async def get_location(request: Request):
    client_host = request.client.host
    response = requests.get(f"https://ipinfo.io/{client_host}/json")
    if response.status_code != 200:
        raise HTTPException(
            status_code=500, detail="Could not retrieve location information"
        )
    return response.json()


@app.post("/sport-query")
async def sport_query(request: SportRequest):
    sport_keywords = [
        "sport",
        "game",
        "match",
        "team",
        "player",
        "score",
        "tournament",
        "league",
        "football",
        "soccer",
        "basketball",
        "cricket",
        "tennis",
        "golf",
        "baseball",
        "hockey",
        "rugby",
        "athletics",
        "swimming",
        "cycling",
        "boxing",
        "wrestling",
        "gymnastics",
        "volleyball",
        "badminton",
        "table tennis",
        "skiing",
        "snowboarding",
        "skating",
        "surfing",
        "karate",
        "judo",
        "taekwondo",
        "fencing",
        "archery",
        "rowing",
        "sailing",
        "canoeing",
        "kayaking",
        "diving",
        "equestrian",
        "triathlon",
        "cricket",
        "bat",
        "ball",
        "wicket",
        "bowler",
        "batsman",
        "fielder",
        "umpire",
        "innings",
        "over",
        "run",
        "boundary",
        "six",
        "four",
        "catch",
        "stump",
        "lbw",
        "test match",
        "one day",
        "t20",
        "ipl",
        "bbl",
        "psl",
        "cpl",
        "ashes",
    ]
    if not any(keyword in request.sport_query.lower() for keyword in sport_keywords):
        raise HTTPException(status_code=400, detail="Query is not related to sports")
    response = gemini_pro_sport_response(request.sport_query)
    return {"response": response}
