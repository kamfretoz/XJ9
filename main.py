#!/usr/bin/env python3

import os
import aiohttp
import hikari
import lightbulb
import miru
import concurrent.futures
from random import choice
from utils.quotes import statuses
from lightbulb.ext import tasks
from utils.const import INTENTS, GUILDS, CACHE, TOKEN, PREFIX

bot = lightbulb.BotApp(
    TOKEN,
    default_enabled_guilds=GUILDS,
    prefix=lightbulb.when_mentioned_or(PREFIX),
    intents=INTENTS,
    cache_settings=CACHE,
    help_slash_command=True,
    ignore_bots=True,
    case_insensitive_prefix_commands=True,
    logs={
        "version": 1,
        "incremental": True,
        "loggers": {
            "hikari": {"level": "INFO"},
            "lightbulb": {"level": "INFO"},
        },
    },
)

miru.load(bot)
tasks.load(bot)

@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    bot.d.aio_session = aiohttp.ClientSession()
    bot.d.process_pool = concurrent.futures.ProcessPoolExecutor()

@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    await bot.d.aio_session.close()
    bot.d.process_pool.shutdown(wait=True)

bot.load_extensions_from("./extensions/", must_exist=True, recursive=True)
bot.load_extensions_from("./meta/", must_exist=True, recursive=True)
bot.load_extensions("lightbulb.ext.filament.exts.superuser")


if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name=choice(statuses),
            type=hikari.ActivityType.WATCHING)
    )
