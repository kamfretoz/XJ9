import lightbulb
import asyncio
from io import BytesIO
from utils.masks import ellipse
from utils.text_wrapper import wrap_text
from PIL import Image, ImageFont
from pilmoji import Pilmoji

font_content = ImageFont.truetype("res/quote/NotoSansCJKjp-Regular.ttf", 18)
font_name    = ImageFont.truetype("res/quote/NotoSansCJKjp-Medium.ttf", 20)

def image_processing(pfp: BytesIO, name: str , content: str):
    with Image.new(mode = "RGBA", size = (700, 300), color = (0, 0 ,0)) as base:
        icon = Image.open(pfp)
        icon.convert("RGBA")
        icon = icon.resize((200, 200), reducing_gap=3.0, resample=Image.Resampling.LANCZOS)
        
        mask = ellipse(icon.size)
        
        base.paste(icon, (30, 30), mask)
        
        text = wrap_text(font=font_content, text=content, max_width=425, max_height=250)
        
        with Pilmoji(base) as final:
            final.text((250, 10), text, font=font_content, align = "left")
            final.text((80, 250), f"{name}", font=font_name, align = "center")
    
    image = BytesIO()
    base.save(image, format="PNG", optimize=True, quality=100)
    image.seek(0)
    return image

aquote_plugin = lightbulb.Plugin("makequote", "Say wha?", include_datastore=True)

@aquote_plugin.command()
@lightbulb.add_cooldown(2, 3, lightbulb.UserBucket)
@lightbulb.set_max_concurrency(2, lightbulb.GuildBucket)
@lightbulb.set_help(text="Please pick a message by replying to them whilst running this command")
@lightbulb.command("Make Quote!", "Create a quote from someone's message", auto_defer = True)
@lightbulb.implements(lightbulb.MessageCommand)
async def makequote(ctx: lightbulb.Context) -> None:
    message = ctx.options.target
    author = message.author
    
    user = ctx.bot.cache.get_member(ctx.get_guild(), author)
    
    content = message.content


    name = user.username
    if not name:
        name = "Unknown User"

    pfp = user.guild_avatar_url or user.avatar_url or user.default_avatar_url   

    if content is None:
        content = " "
    
    user_pfp = BytesIO()
    
    async with pfp.stream() as reader:
        async for chunk in reader:
            user_pfp.write(chunk)
    
    loop = asyncio.get_running_loop()
    img = await loop.run_in_executor(ctx.bot.d.process_pool, image_processing, user_pfp, name, content.strip())

    await ctx.respond(attachment=img, content = f"Here is the quote! {ctx.author.mention}", user_mentions=True)

def load(bot):
    bot.add_plugin(aquote_plugin)

def unload(bot):
    bot.remove_plugin(aquote_plugin)
