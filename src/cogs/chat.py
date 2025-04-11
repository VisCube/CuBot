from discord import ApplicationContext, Bot, Cog, Message, message_command

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


def setup(bot: Bot):
    bot.add_cog(Chat(bot))
