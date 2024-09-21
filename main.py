# main.py
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    today: str
    ageat: str


@app.post("/age/")
async def create_item(item: Item):
    # URL of the third-party API call
    third_party_url = f"https://www.calculator.net/age-calculator.html?today={item.today}&ageat={item.ageat}&x=Calculate"
    response = requests.get(third_party_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Scrape result text
    p_tag = soup.find("p", class_="verybigtext")
    age_text = p_tag.get_text(separator=' ').strip()

    return {
        "message": age_text
    }
