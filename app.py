from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import joblib
import uvicorn
import texthelper as th

app = FastAPI()
model = joblib.load("./model/spam-classifier.joblib")


def classify_message(model, message):
    message = th.preprocessor(message)
    label = model.predict([message])[0]
    spam_proba = model.predict_proba([message])
    return {"label": label, "spam_probability": spam_proba[0][1]}


@app.get("/")
def docs():
    return RedirectResponse(url="/docs")


@app.get("/predict")
async def predict_get(message: str):
    return classify_message(model, message)


class Message(BaseModel):
    message: str


@app.post("/predict")
async def predict_post(req: Message):
    return classify_message(model, req.message)


if __name__ == "__main__":
    uvicorn.run(app)
