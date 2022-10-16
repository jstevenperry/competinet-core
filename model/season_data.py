#
# Base class for a single season's worth of data

from model.base_model import BaseModel


class SeasonData(BaseModel):
    __slots__ = [
        "period", "team_name"
    ]

    def __init__(self, period, team_name):
        self.period = period
        self.team_name = team_name


