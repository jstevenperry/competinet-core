#
# The base class for all model objects
import json


class BaseModel:
    """
    The base class for all model objects
    """
    def to_json(self):
        return json.dumps(self, default=lambda me: me.__dict__)

