import typing

from ellar.common import Serializer


class TodoSerializer(Serializer):
    id: typing.Optional[int]
    title: str
    description: str
    status_completed: bool
    user_id: int


class RetrieveTodoSerializer(TodoSerializer):
    pk: str







