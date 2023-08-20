import strawberry
from strawberry_django.optimizer import DjangoOptimizerExtension
from .query import Query
# from .mutate import Mutation
# from strawberry_django_jwt.middleware import JSONWebTokenMiddleware

schema = strawberry.Schema(
    query=Query,
    # mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
        # JSONWebTokenMiddleware,
    ],
)