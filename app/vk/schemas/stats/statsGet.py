"""
Pydantic schemas for VK.Stats.Get
"""

from pydantic import BaseModel
from typing import Optional, List


class VKStatsGetRequest(BaseModel):
    """
    Pydantic schema for VK.Stats.Get requests.
    """
    group_id: Optional[int] = None
    app_id: Optional[int] = None
    timestamp_from: Optional[int] = None
    timestamp_to: Optional[int] = None
    interval: Optional[str] = None
    intervals_count: Optional[int] = None
    filters: Optional[str] = None
    stats_groups: Optional[str] = None
    extended: Optional[str] = None

    class Config:
        from_attributes = True


class City(BaseModel):
    count: int
    name: str
    value: int


class Country(BaseModel):
    code: str
    count: int
    name: str
    value: int


class Sex(BaseModel):
    value: str
    count: int


class Age(BaseModel):
    value: str
    count: int


class SexAge(BaseModel):
    value: str
    count: int


class Activity(BaseModel):
    comments: Optional[int] = None
    copies: Optional[int] = None  # Рассказали друзьям
    hidden: Optional[int] = None
    likes: Optional[int] = None
    subscribed: Optional[int] = None
    unsubscribed: Optional[int] = None


class Reach(BaseModel):
    age: Optional[List[Age]] = []
    cities: Optional[List[City]] = []
    countries: Optional[List[Country]] = []
    sex: Optional[List[Sex]] = []
    sex_age: Optional[List[SexAge]] = []
    mobile_reach: Optional[int] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None


class Visitors(BaseModel):
    age: Optional[List[Age]] = []
    cities: Optional[List[City]] = []
    countries: Optional[List[Country]] = []
    sex: Optional[List[Sex]] = []
    sex_age: Optional[List[SexAge]] = []
    mobile_views: Optional[int] = None
    views: Optional[int] = None
    visitors: Optional[int] = None


class Stats(BaseModel):
    activity: Optional[Activity] = Activity()
    reach: Optional[Reach] = Reach()
    visitors: Optional[Visitors] = Visitors()
    period_from: int
    period_to: int


class VKStatsGetResponse(BaseModel):
    """
    Pydantic schema for VK.Stats.Get responses.

    https://dev.vk.com/ru/method/stats.get
    """
    response: List[Stats]
