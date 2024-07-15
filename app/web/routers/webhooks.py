from fastapi import APIRouter
from aiohttp import web
from aiogram import types
from app.bot.loader import bot
from app.bot.loader import dp
from app.config import load_config, webhook_settings
from fastapi import Request, HTTPException

router = APIRouter()
webhook_path = webhook_settings(load_config)['webhook_path']


@router.post(webhook_path)
async def webhook_endpoint(request: Request):
    return await handle_webhook(request)


async def handle_webhook(request: Request):
    bot_token = load_config().bot.token
    url = str(request.url)
    index = url.rfind('/')
    token = url[index + 1:]
    
    if token == bot_token:
        update = types.Update(**await request.json())
        await dp.feed_webhook_update(bot, update)
        return web.Response()
    else:
        raise HTTPException(status_code=403, detail="Forbidden")
