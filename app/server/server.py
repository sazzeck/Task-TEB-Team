import asyncio

import uvicorn

from django.core.asgi import get_asgi_application

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


class MyServer:
    app = get_asgi_application

    config = uvicorn.Config(app=app, loop=loop, port=8080)
    server = uvicorn.Server(config=config)

    @classmethod
    def run(cls):
        asyncio.run(cls.on_startup())
        asyncio.run(cls.server.serve())
        asyncio.run(cls.on_shutdown())

    @staticmethod
    async def on_startup() -> None:
        pass

    @staticmethod
    async def on_shutdown() -> None:
        pass
