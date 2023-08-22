import strawberry
from strawberry_django.optimizer import DjangoOptimizerExtension
from .query import Query
from .mutate import Mutation
from gqlauth.core.middlewares import JwtSchema


schema = JwtSchema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
    ],
)