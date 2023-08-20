import strawberry
from .types import TmpType

@strawberry.type
class Query:
    tmps: list[TmpType] = strawberry.django.field()