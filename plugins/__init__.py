# Don't Remove Credit @Tech_Shreyansh29
# Subscribe YouTube Channel For Amazing Bot @TechShreyansh
# Ask Doubt on telegram @SmartEdith_Bot

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
