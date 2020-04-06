import asyncio
from channels.generic.http import AsyncHttpConsumer
from channels.generic.websocket import WebsocketConsumer


class Events(WebsocketConsumer):
    def connect(self, *args, **kwargs):
        print(args, kwargs)
        self.accept()