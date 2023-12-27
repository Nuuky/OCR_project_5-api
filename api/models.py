from typing import Optional
from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    class Config:
        anystr_strip_whitespace = True
        require_by_default = False


class Status(CustomBaseModel):
    version: str
    success: bool
    reason: Optional[str]


class BaseResponse(CustomBaseModel):
    success: bool
    reason: Optional[str]


class PredictionResponse(BaseResponse):
    topics: list[str]


class PredictionRequest(CustomBaseModel):
    text: str
