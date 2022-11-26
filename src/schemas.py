from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Friend(BaseModel):
    id: int
    name: str


class Output(BaseModel):
    _id: str
    index: int
    guid: str
    isActive: bool
    balance: str
    picture: str
    age: int
    eyeColor: str
    name: str
    gender: str
    company: str
    email: str
    phone: str
    address: str
    about: str
    registered: str
    latitude: float
    longitude: float
    tags: List[str]
    friends: List[Friend]
    greeting: str
    favoriteFruit: str
