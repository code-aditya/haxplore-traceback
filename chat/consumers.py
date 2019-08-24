from channels.generic.websocket import AsyncJsonWebsocketConsumer
from chat import models
from channels.db import database_sync_to_async


class ChatConsumer(AsyncJsonWebsocketConsumer):
    MESSAGE_TYPE_NEW_CHAT = 'chat.msg.new_chat'
    MESSAGE_TYPE_NEW_MESSAGE = 'chat.msg.new_message'
    # MESSAGE_TYPE_UPDATE_MESSAGE = 'chat.msg.update_message'
    MESSAGE_TYPE_LIST_CHATS = 'chat.msg.list_chats'
    MESSAGE_TYPE_LIST_MESSAGES = 'chat.msg.list_messages'

    COMMAND_LIST_CHATS = 'chat.cmd.list_chats'
    COMMAND_CHAT_LIST_MESSAGES = 'chat.cmd.list_messages'
    COMMAND_CHAT_SEND_MESSAGE = 'chat.cmd.send_message'
    COMMAND_NEW_CHAT = 'chat.cmd.new_chat'
    COMMAND_DELETE_CHAT = 'chat.cmd.delete_chat'
    COMMAND_CHAT_DELETE_MESSAGE = 'chat.cmd.delete_message'

    async def connect(self):
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            return
        if await self.update_client():
            await self.accept()
            await self.initialize()

    async def initialize(self):
        await self.list_chats()
        # await self.join_chats()

    @database_sync_to_async
    def clear_client(self):
        models.Client.objects.filter(user=self.user).update(channel_chat=None)

    async def disconnect(self, code):
        await self.clear_client()

    @database_sync_to_async
    def update_client(self):
        clients = models.Client.objects.filter(user=self.user)
        if clients:
            clients.update(channel_chat=self.channel_name)
            return True
        return False

    async def chat_send_message(self, event):
        await self.send_json({
            "type": ChatConsumer.MESSAGE_TYPE_NEW_MESSAGE,
            "chat": event['chat'],
            "data": event['data'],
            "is_self": False #TODO
        })

    @database_sync_to_async
    def _find_chats_for_user(self, user):
        expert_qs = models.ExpertChat.objects.find_for_user(user)
        farmer_qs = models.FarmerChat.objects.find_for_user(user)
        return [expert.chat for expert in expert_qs] + [farmer.chat for farmer in farmer_qs]

    async def list_chats(self):
        chats = await self._find_chats_for_user(self.user)
        data = [
            {
                "id": chat.id,
                "name": chat.name,
                "target_user": chat.get_target_user(self.user).first_name
            }
            for chat in chats
        ]
        await self.send_json({
            "type": ChatConsumer.MESSAGE_TYPE_LIST_CHATS,
            "data": data
        })

    async def receive_json(self, content, **kwargs):
        command = content.pop('command')
        chat_id = content.get('chat_id', None)
        if command == ChatConsumer.COMMAND_LIST_CHATS:
            await self.list_chats()
        elif command == ChatConsumer.COMMAND_CHAT_LIST_MESSAGES:
            self.list_chat_messages(chat_id)
        elif command == ChatConsumer.COMMAND_NEW_CHAT:
            self.create_or_join_chat(content)
        elif command == ChatConsumer.COMMAND_DELETE_CHAT:
            self.delete_chat(chat_id)
        elif command == ChatConsumer.COMMAND_CHAT_SEND_MESSAGE:
            msg = content.get('message')
            self.chat_send_message(chat_id, msg)
        else:
            print(f'Unsupported command: {command}')
