from io import BytesIO

import openai
from discord import Attachment, File
from openai.types.audio import Transcription


async def transcribe(attachment: Attachment) -> Transcription:
    data = BytesIO(await attachment.read())
    data.name = attachment.filename

    return openai.audio.transcriptions.create(
        file=data,
        model="whisper-1"
    )


def voice(text: str) -> File:
    response = openai.audio.speech.create(
        input=text,
        model="tts-1",
        voice="echo"
    )
    data = BytesIO(response.read())

    return File(fp=data, filename="voice.mp3")
