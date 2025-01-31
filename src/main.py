import os

from dotenv import load_dotenv

import pycord_api

if __name__ == "__main__":
    load_dotenv()
    pycord_api.run(token=os.getenv("DISCORD_TOKEN"))
