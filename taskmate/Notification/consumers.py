import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
        #btfta7 websocket connection between server and user(here the user is the reciever)
    async def connect(self):
                #mn el routing url 
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.group_name = f"user_{self.user_id}"

        print(self.channel_layer.__dict__)
        print('/n/n')
        # if self.group_name not in self.channel_layer.groups:
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        print(f"User {self.user_id} connected to WebSocket group {self.group_name}")


    async def send_notification(self, event):
        # Send the message to the connected WebSocket client
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def disconnect(self, close_code):
        # Remove the user from the WebSocket group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print(f"User {self.user_id} disconnected from WebSocket group {self.group_name}")

