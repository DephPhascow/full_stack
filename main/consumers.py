import json
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from main.models import UserModel
import logging

logger = logging.getLogger(__name__)
     
class WebSocketTmpConsumer(AsyncWebsocketConsumer):        
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await get_channel_layer().send(self.channel_name, {
            "type": "send.sdp",
            "data": {'channel': self.channel_name},
        })
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        print("#######", data_json)
        
        data_json['channel'] = self.channel_name
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send.sdp',
                'data': data_json,
            }
        )

    async def send_sdp(self, event):
        receive = event['data']
        await self.send(text_data=json.dumps(receive))

    async def call_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def call(self, data):
        try:
            callee = await sync_to_async(UserModel.objects.get)(login=data['login'])
        except UserModel.DoesNotExist:
            return 'None', {"type": "chat.message", 'message': 'User does not connected!'}

        return callee.channel_name, {
            "type": "chat.message",
            'calling': 'ok',
            'callee': callee.login,
            'room': self.room_name
        }