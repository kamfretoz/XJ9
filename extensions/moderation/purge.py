import hikari
import lightbulb
import miru
from datetime import datetime, timedelta, timezone
from hikari.permissions import Permissions

purge_plugin = lightbulb.Plugin("purge", "Burn down the evidence! *evil laugh*")
purge_plugin.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES),
    lightbulb.guild_only
)
PURGE_PERMISSIONS = (
    Permissions.MANAGE_MESSAGES
)


async def purge_messages(ctx: lightbulb.Context, amount: int, channel: hikari.Snowflakeish) -> None:
    iterator = (
                ctx.bot.rest.fetch_messages(channel)
                .limit(amount)
                .take_while(lambda msg: (datetime.now(timezone.utc) - msg.created_at) < timedelta(days=14))
            )
    if iterator:
        async for messages in iterator.chunk(100):
            await ctx.bot.rest.delete_messages(channel, messages)
        await ctx.respond(f"**Messages has been sucessfully deleted.**", delete_after=5)
    else:
        await ctx.respond("Could not find any messages younger than 14 days!")
class PromptView(miru.View):
    async def view_check(self, ctx: miru.Context) -> bool:
        return ctx.user.id == ctx.message.interaction.user.id

class ConfirmButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.DANGER, label="Confirm")
    async def callback(self, ctx: miru.Context) -> None:
        # You can access the view an item is attached to by accessing it's view property
        self.view.accepted = True
        self.view.stop()
    
class CancelButton(miru.Button):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(style=hikari.ButtonStyle.SUCCESS, label="Cancel")

    async def callback(self, ctx: miru.Context) -> None:
        self.view.accepted = False
        self.view.stop()

@purge_plugin.command
@lightbulb.add_cooldown(3, 3, lightbulb.UserBucket)
@lightbulb.option("amount", "The number of messages to purge.", type=int, required=True, max_value = 500)
@lightbulb.app_command_permissions(PURGE_PERMISSIONS, dm_enabled=False)
@lightbulb.command("purge", "Purge messages from this channel.", aliases=["clear","prune"], auto_defer = True, pass_options = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def purge(ctx: lightbulb.Context, amount: int) -> None:
    if amount > 500:
        await ctx.respond(":x: **You can only purge 500 messages at once, max**")
        return
    
    channel = ctx.channel_id

    # If the command was invoked using the PrefixCommand, it will create a message
    # before we purge the messages, so you want to delete this message first
    if isinstance(ctx, lightbulb.PrefixContext):
        await ctx.event.message.delete()

    pruneview = PromptView(timeout=30, autodefer=True)
    pruneview.add_item(ConfirmButton())
    pruneview.add_item(CancelButton())
    
    prompt = await ctx.respond("Are you sure you want to continue the prune operation? **__This Action is irreversible.__**", components=pruneview.build(), flags=hikari.MessageFlag.EPHEMERAL)
    msg = await prompt.message()
    pruneview.start(msg)
    await pruneview.wait()
    
    if hasattr(pruneview, "accepted"):
        if pruneview.accepted is True:
            await prompt.delete()
            await purge_messages(ctx, amount, channel)
        elif pruneview.accepted is False:
            await prompt.delete()
            await ctx.respond(f"**Prune Operation has been cancelled.**", delete_after=7)
    else:
        await prompt.delete()
        await ctx.respond(f"**Prune Operation has been cancelled due to inactivity.**", delete_after=7)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(purge_plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(purge_plugin)