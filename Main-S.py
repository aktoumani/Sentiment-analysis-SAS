from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline

# Charger le modèle Hugging Face
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_model = pipeline("sentiment-analysis", model=model_name)

# Configurer l'application FastAPI
app = FastAPI()

# Configurer Jinja2 pour les templates HTML
templates = Jinja2Templates(directory="templates")

class TextInput(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    """Afficher le formulaire HTML"""
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/analyze/")
def analyze_sentiment(text: str = Form(...)):
    """Analyser le sentiment du texte soumis"""
    result = sentiment_model(text)
    return {
        "text": text,
        "sentiment": result[0]["label"],
        "confidence": round(result[0]["score"], 2)
    }
