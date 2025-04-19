from discord import ApplicationContext, Bot, Cog, Message, message_command

from src.openai.audio import transcribe


class Audio(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @message_command(name="Whisper")
    async def whisper(self, context: ApplicationContext, message: Message):
        await context.defer(ephemeral=True)

        attachments = [
            attachment for attachment in message.attachments
            if attachment.content_type.split("/")[0] in ("audio", "video")
        ]

        if not attachments:
            await context.respond("No transcribable attachments found.")

        for attachment in attachments:
            transcription = await transcribe(attachment=attachment)
            await context.respond(content=transcription.text, ephemeral=True)


def setup(bot: Bot):
    bot.add_cog(Audio(bot))
