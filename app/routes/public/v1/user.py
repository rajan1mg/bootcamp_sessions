from sanic import Blueprint, Request

from app.decorators.validate_signup import validate_signup
from app.managers.user import UserManager
from app.request_validation import UserSignup
from utils.response import success

user_bp = Blueprint("user", url_prefix="/users")


@user_bp.post("/signup")
@validate_signup
async def signup(_request: Request):
    signup_params = UserSignup(**_request.json).dict()
    response = await UserManager.signup(signup_params)
    return success(response, status_code=200)



