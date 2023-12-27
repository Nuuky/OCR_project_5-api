from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from api.models import Status, PredictionRequest, PredictionResponse
from api.nlp import get_topics_from_text, get_topics_from_html

app = FastAPI(
    title="NLP topic prediction API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status", response_model=Status)
def get_status():
    return Status(version="0.1.0", success=True)


@app.post("/predict_text", response_model=PredictionResponse, tags=["NLP"])
async def predict_text(body: PredictionRequest):
    try:
        topics = get_topics_from_text(body.text)
        print(topics)
        return PredictionResponse(topics=topics, success=True)
    except Exception as e:
        return PredictionResponse(topics=[], success=False, reason=str(e))


@app.post("/predict_html", response_model=PredictionResponse, tags=["NLP"])
async def predict_html(body: PredictionRequest):
    try:
        topics = get_topics_from_html(body.text)
        return PredictionResponse(topics=topics, success=True)
    except Exception as e:
        return PredictionResponse(topics=[], success=False, reason=str(e))
