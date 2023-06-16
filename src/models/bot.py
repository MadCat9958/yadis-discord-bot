import discord
from discord.ext import commands
from typing import Optional
import custom_logs
from asyncio import run as async_run


class Yadis(commands.Bot):
    def __init__(self, debug_channel_id: int, intents: int, token: Optional[str] = None, *args, **kwargs):
        super().__init__(
            case_insensitive=False,
            strip_after_prefix=True,
            help_command=None,
            intents=discord.Intents(intents),
            *args,
            **kwargs
        )
        self.token = token
        self.debug_channel = self.get_channel(debug_channel_id)
        self.logger = custom_logs.Logger("Bot", self)

    async def on_ready(self):
        await self.logger.info("Ready!", to_file=False)

    def run(self, token: Optional[str] = None):
        async_run(self.logger.sucsess("Locked and loaded!", to_file=False, to_channel=False))
        async_run(self.logger.info("Starting...", to_file=False, to_channel=False))
        super().run(token or self.token, log_handler=None)
