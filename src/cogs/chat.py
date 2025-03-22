from discord import ApplicationContext, Bot, Cog, Message, message_command
from discord.ext import commands

from src.openai.chat import complete


class Chat(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @message_command(name="ChatGPT")
    async def chatgpt(self, context: ApplicationContext, message: Message):
        await context.defer(ephemeral=True)

        completion = await complete(messages=(message,))
        content = completion.choices[0].message.content

        await context.respond(content=content)

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot or not self.bot.user.mentioned_in(message):
            return

        history = message.channel.history()
        thread, latest = [message], message
        while latest.reference is not None:
            latest = await history.get(id=latest.reference.message_id)
            if latest is None:
                break
            thread.insert(0, latest)

        async with message.channel.typing():
            completion = await complete(messages=thread)
            content = completion.choices[0].message.content
            await message.reply(content=content)


def setup(bot: Bot):
    bot.add_cog(Chat(bot))
