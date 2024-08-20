from datetime import date, datetime
from decimal import Decimal
from typing import Annotated
from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator


def parse_date(value: str):
    return datetime.strptime(
        value,
        "%d.%m.%Y"
    ).date()


def str_date_encoder(value: date):
    return value.strftime("%d.%m.%Y")


class QuerySchema(BaseModel):
    date: Annotated[date, BeforeValidator(parse_date)]
    periods: Annotated[int, Field(ge=1, le=60)]
    amount: Annotated[int, Field(ge=10000, le=3000000)]
    rate: Annotated[float, Field(ge=1, le=8)]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "date": "30.01.2020",
                    "periods": 7,
                    "amount": 10000,
                    "rate": 6,
                }
            ]
        }
    }


class MonthDeposite(BaseModel):
    date: date
    amount: Decimal

    class Config:
        json_encoders = {
            date: str_date_encoder
        }
