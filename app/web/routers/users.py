import logging
from urllib.parse import quote, unquote

from fastapi import APIRouter, Depends, Form, Request
from starlette.exceptions import HTTPException
from starlette.responses import RedirectResponse

from app.config import templates
from app.store.database.models import User
from app.store.database.queries.rooms import RoomDB
from app.store.database.queries.users import UserDB
from app.web.dependencies import get_current_user

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/profile/{user_id}", name='profile')
async def profile(request: Request, user_id: int,
                  current_user: User = Depends(get_current_user)):
    
    # TODO add permissions [superuser | owner_profile]
    
    user = await UserDB.get_user_or_none(user_id)
    
    if not user:
        raise HTTPException(status_code=404)
    
    rooms = await RoomDB.get_all_users_of_room(user_id)
    
    context = {
        'request': request,
        'current_user': current_user,
        'user': user,
        'rooms': rooms,
    }
    
    return templates.TemplateResponse(
        'users//profile.html', context=context
    )


@router.get("/users", name='users')
async def users(request: Request,
                current_user: User = Depends(get_current_user)):
    # TODO add permissions [superuser]
    users = await UserDB.get_list_all_users()
    context = {
        'request': request,
        'current_user': current_user,
        'users': users,
    }
    return templates.TemplateResponse(
        'users//users.html', context=context
    )


@router.post("/user/activate/{user_id}", name='activate_user')
async def activate(request: Request, user_id: int,
                   current_user: User = Depends(get_current_user)):
    # TODO add permissions [superuser]
    
    user = await UserDB.get_user_or_none(user=user_id)
    if not user:
        raise HTTPException(status_code=404)
    
    if user.is_active:
        await  UserDB.disable_user(user_id)
    else:
        await  UserDB.enable_user(user_id)
    
    referer = request.headers.get('referer')
    return RedirectResponse(url=referer, status_code=301)


@router.get("/user/{user_id}/delete_confirmation/", name='usr_del_confirmation')
async def index(request: Request, user_id: int,
                current_user: User = Depends(get_current_user)):
    # TODO add permissions [superuser]
    user = await UserDB.get_user_or_none(user_id)
    context = {
        'request': request,
        'current_user': current_user,
        "user": user,
        'referer': quote(request.headers.get('referer'), safe='')
    }
    
    return templates.TemplateResponse(
        'users//delete_confirmation.html', context=context)


@router.post("/user/delete/", name='delete_user')
async def delete(request: Request, user_id: int = Form(...),
                 referer: str = Form(...), confirm: bool = Form(...),
                 current_user: User = Depends(get_current_user)):
    # TODO add permissions [superuser]
    if confirm:
        await UserDB.delete_user(user_id)
    
    return RedirectResponse(url=unquote(referer), status_code=301)
