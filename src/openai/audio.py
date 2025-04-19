from io import BytesIO

import openai
from discord import Attachment
from openai.types.audio import Transcription


async def transcribe(attachment: Attachment) -> Transcription:
    data = BytesIO(await attachment.read())
    data.name = attachment.filename

    return openai.audio.transcriptions.create(
        file=data,
        model="whisper-1"
    )
