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


class Activity(BaseModel):
    comments: Optional[int] = None
    likes: Optional[int] = None
    subscribed: Optional[int] = None


class City(BaseModel):
    count: int
    name: str
    value: int


class Country(BaseModel):
    code: str
    count: int
    name: str
    value: int


class Reach(BaseModel):
    cities: List[City]
    countries: List[Country]
    mobile_reach: int
    reach: int
    reach_subscribers: int


class Visitors(BaseModel):
    cities: List[City]
    countries: List[Country]
    mobile_views: int
    views: int
    visitors: int


class Stats(BaseModel):
    activity: Optional[Activity] = []
    period_from: int
    period_to: int
    reach: Reach
    visitors: Visitors


class VKStatsGetResponse(BaseModel):
    """
    Pydantic schema for VK.Stats.Get responses.

    https://dev.vk.com/ru/method/stats.get
    """
    response: List[Stats]
