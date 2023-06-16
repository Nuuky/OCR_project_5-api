from typing import Optional, Union
from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    class Config:
        anystr_strip_whitespace = True
        require_by_default = False


class Status(CustomBaseModel):
    version: str
    success: bool
    reason: Optional[str]


class Topic(CustomBaseModel):
    name: str
    proba: Optional[float]


class BaseResponse(CustomBaseModel):
    data: dict
    success: bool
    reason: Optional[str]


class Prediction(CustomBaseModel):
    topics: list[Topic]


class PredictionResponse(BaseResponse):
    data: Prediction


class PredictionRequest(CustomBaseModel):
    text: str
    max_topics: int
