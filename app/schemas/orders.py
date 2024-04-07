from uuid import UUID, uuid4

from enum import Enum
from pydantic import BaseModel, field_validator


class DrinkEnum(str, Enum):
    coffee: str = "coffee"
    soda: str = "soda"
    beer: str = "beer"
    wine: str = "wine"


class MealEnum(str, Enum):
    pasta: str = "pasta"
    pizza: str = "pizza"
    meat: str = "meat"
    fish: str = "fish"


class DessertEnum(str, Enum):
    cookie: str = "cookie"
    donut: str = "donut"
    brownie: str = "brownie"
    gelato: str = "gelato"


class OrderBase(BaseModel):
    order_id: UUID = uuid4()


class OrderCreate(OrderBase):
    drink: DrinkEnum
    meal: MealEnum
    dessert: DessertEnum


class OrderRead(OrderBase):
    drink: str
    meal: str
    dessert: str
