from dataclasses import dataclass
from typing import Any

from broadcaster import Broadcast

broadcast = None


async def get_broadcast():
    global broadcast

    if not broadcast:
        broadcast = Broadcast("memory://")

        await broadcast.connect()

    return broadcast


@dataclass
class Context:
    broadcast: Broadcast
    request: Any