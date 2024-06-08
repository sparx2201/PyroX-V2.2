# import pyrogram
# import strings
# import config

# from Barath import bot, barath
# from Barath.helpers.help_func import get_datetime

# async def run_clients():
#     await bot.start()
#     await barath.start()
#     await pyrogram.idle()
#     zone = await get_datetime()
#     await bot.send_message(
#         chat_id=config.GROUP_ID,
#         text=strings.RESTART_TEXT1.format(date=zone["date"], time=zone["time"]))
#     await barath.send_message(
#         chat_id=config.GROUP_ID,
#         text=strings.RESTART_TEXT2.format(date=zone["date"], time=zone["time"]))

# if __name__ == "__main__":
#     barath.loop.run_until_complete(run_clients())



import os
import asyncio
import logging
import pyrogram
import strings
import config

from Barath import bot, barath
from Barath.helpers.help_func import get_datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_clients():
    try:
        # Start the bot and barath clients
        await bot.start()
        await barath.start()
        logger.info("Bot and Barath started successfully")

        # Keep the bot running
        await pyrogram.idle()

        # Send restart messages
        zone = await get_datetime()
        await bot.send_message(
            chat_id=config.GROUP_ID,
            text=strings.RESTART_TEXT1.format(date=zone["date"], time=zone["time"]))
        await barath.send_message(
            chat_id=config.GROUP_ID,
            text=strings.RESTART_TEXT2.format(date=zone["date"], time=zone["time"]))
        
        # Stop the bot and barath clients
        await bot.stop()
        await barath.stop()
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(run_clients())
