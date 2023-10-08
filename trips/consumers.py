from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async


# @database_sync_to_async
# def _get_user_group(self, user):
#     return user.groups.first().name


class TaxiConsumer(AsyncJsonWebsocketConsumer):
    groups = ['test']  
    
    @database_sync_to_async
    def _get_user_group(self, user):
        group = user.groups.first()
        if group:
            return group.name
        
        return None
          
    
    async def connect(self):
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
        else:
            user_group = await self._get_user_group(user)
            if user_group == 'driver':
                await self.channel_layer.group_add(
                    group='test',
                    channel=self.channel_name
                )
            await self.accept()
        
        
    async def receive_json(self, content, **kwargs):
        message_type = content.get('type')
        if message_type == 'echo.message':
            await self.send_json({
                'type': message_type,
                'data': content.get('data',)
            })
            
            
    async def echo_message(self, message):
        await self.send_json({
            'type': message.get('type'),
            'data': message.get('data'),
        })
        
        
    async def disconnect(self, code):
        user = self.scope['user']
        user_group = await self._get_user_group(user)
        if user_group == 'driver':
            await self.channel_layer.group_discard(
                group='test',
                channel=self.channel_name
            )
        await super().disconnect(code)
        
        
