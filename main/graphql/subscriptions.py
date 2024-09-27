import asyncio
from typing import AsyncGenerator
import strawberry
from django.core.serializers import deserialize
from main.graphql.types import TmpType

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def on_message(self, info) -> AsyncGenerator[None, str]:
        print("starting on_message")
        print(id(info.context.broadcast))

        async with info.context.broadcast.subscribe(channel="chatroom") as subscriber:
            print(f"{subscriber=}")
            async for event in subscriber:
                print(f"{event=}")
                yield event.message

    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[None, int]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)
    @strawberry.subscription
    async def changed_hero(self, info) -> AsyncGenerator[None, TmpType]:
        async with info.context.broadcast.subscribe(channel="heros") as subscriber:
            async for event in subscriber:
                instance = list(deserialize("json", event.message))[0].object
                # yield instance
                yield TmpType(instance.name, instance.description)