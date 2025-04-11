from typing import Iterable

import openai
from discord import Attachment, Message
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionContentPartImageParam as ImageContent,
    ChatCompletionContentPartParam as Content,
    ChatCompletionContentPartTextParam as TextContent,
    ChatCompletionUserMessageParam as UserMessage
)
from openai.types.chat.chat_completion_content_part_image_param import ImageURL


async def complete(messages: Iterable[Message]) -> ChatCompletion:
    gpt_messages = [await convert_message(message) for message in messages]

    return openai.chat.completions.create(
        messages=gpt_messages,
        model="gpt-4o"
    )


async def convert_message(message: Message) -> UserMessage:
    text = TextContent(text=message.content, type="text")
    media = [await convert_attachment(att) for att in message.attachments]

    return UserMessage(
        content=(text, *media),
        name=str(message.author.id),
        role="user"
    )


async def convert_attachment(attachment: Attachment) -> Content:
    match attachment.content_type.split("/")[0]:
        case "image":
            image_url = ImageURL(url=attachment.url, detail="auto")
            return ImageContent(image_url=image_url, type="image_url")
        case "text":
            data = await attachment.read()
            return TextContent(text=data.decode(), type="text")
        case _:
            return TextContent(text=attachment.filename, type="text")
