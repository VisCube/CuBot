from typing import Iterable

import openai
from discord import Message
from openai.types.chat import ChatCompletion, ChatCompletionUserMessageParam


def complete(messages: Iterable[Message]) -> ChatCompletion:
    gpt_messages = map(convert_message, messages)

    return openai.chat.completions.create(
        messages=gpt_messages,
        model="gpt-4o-mini"
    )


def convert_message(message: Message) -> ChatCompletionUserMessageParam:
    return ChatCompletionUserMessageParam(
        content=message.content,
        name=str(message.author.id),
        role="user"
    )
