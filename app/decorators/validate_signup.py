from sanic import Request

from app.exceptions.validation_exception import ValidationException


def validate_signup(func):
    async def decorator(_request: Request):
        age = _request.json.get("age")
        if age < 18:
            raise ValidationException(message="Age is not over 18")
        return await func(_request)

    return decorator
