"""
MIT License

Copyright (c) 2023 Tumpa-Prizrak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from src.models.bot import Yadis
from src import config
from src import custom_logs
from asyncio import run
from discord.ext.commands import when_mentioned_or


bot_info = config.load_config(config.Configs.bot_info)

log = custom_logs.Logger("Main")
run(log.info(message="Loading...", to_channel=False, to_file=False))

bot = Yadis(
    token=bot_info.get("token"),
    command_prefix=when_mentioned_or(bot_info.get("prefix")),
    owner_id=bot_info.get("owner"),
    debug_channel_id=bot_info.get("debug_channel_id"), # type: ignore
    intents=bot_info.get("intents"), # type: ignore
)

bot.run()
