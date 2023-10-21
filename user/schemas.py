
from ellar.common import Serializer
from datetime import datetime
from pydantic import Field
import typing


class UserSerializer(Serializer):
    id: typing.Optional[int]
    email: str
    name: str
    created_date: datetime = Field(default_factory=datetime.now)
    is_active: bool = Field(default=True)
    hashed_password: str


class RetrieveUserSerializer(UserSerializer):
    pk: str
