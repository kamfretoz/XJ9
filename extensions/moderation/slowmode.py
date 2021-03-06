import lightbulb
import hikari
from hikari.permissions import Permissions

slowmode_plugin = lightbulb.Plugin("slowmode", "*talks in slow motion*")
slowmode_plugin.add_checks(
    lightbulb.checks.has_guild_permissions(hikari.Permissions.MANAGE_CHANNELS),
    lightbulb.checks.bot_has_guild_permissions(hikari.Permissions.MANAGE_CHANNELS)
    )
SLOWMODE_PERMISSIONS = (
    Permissions.MANAGE_CHANNELS
)

@slowmode_plugin.command()
@lightbulb.add_cooldown(3, 3, lightbulb.UserBucket)
@lightbulb.option("interval", "The interval amount (in seconds)", int, min_value = 0, max_value = 21600, required=False)
@lightbulb.option("channel", "The channel you want to set", hikari.TextableGuildChannel, required=True)
@lightbulb.app_command_permissions(SLOWMODE_PERMISSIONS, dm_enabled=False)
@lightbulb.command("slowmode", "Set the slowmode interval for a channel", auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def slowmode(ctx: lightbulb.Context, channel: hikari.TextableGuildChannel, interval: int):
    time = interval or 0
    if time == 0:
        await ctx.respond(f"Removing slow mode from the selected channel")
    else:
        await ctx.respond(f"Attempting to set slowmode on the selected channel for **{time} seconds**")
    await ctx.bot.rest.edit_channel(channel, rate_limit_per_user=time)
    await ctx.edit_last_response(f"Slowmode of {time} second(s) has been set for {channel.mention}")
    
def load(bot):
    bot.add_plugin(slowmode_plugin)

def unload(bot):
    bot.remove_plugin(slowmode_plugin)
