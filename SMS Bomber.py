from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
def register(cb):
    cb(BomberMod())
class BomberMod(loader.Module):
    """Bomber"""
    strings = {'name': 'Bomber'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()
    async def bombacmd(self, message):
        """.bomba
           Формат номера: 380959559595 7999999990 (без +)
        """
        reply = await message.get_reply_message()
        if not reply:
            if utils.get_args_raw(message):
                user = utils.get_args_raw(message)
            else:
                await message.edit("<b>Какой номер?</b>")
                return
        else:
            try:
                user = str(reply.text)
            except:
                await message.edit("<b>Err</b>")
                return
        await message.edit("<b>СМС...</b>")
        chat = '@smsbomberos_bot'
        async with message.client.conversation(chat) as conv:
            try:
                await message.edit("<b>Обработка...</b>")
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1323142275))
                m1 = await message.client.send_message(chat, "/dehash {0}".format(user))
                m2 = response = await response
            except YouBlockedUserError:
                await message.edit('<code>Unblock</code> ' + chat)
                return
            await m1.delete()
            if(response.text.startswith("⚠️")):
                await message.edit("⚠️ Ничего не найдено")
            else:
                await message.edit(response.text)
            await m2.delete()