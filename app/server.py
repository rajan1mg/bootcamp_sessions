from sanic import Sanic, json, Request

from app.routes import blueprint_group
from utils.config import CONFIG
config = CONFIG.config
app = Sanic(name=config.get("NAME"))
app.blueprint(blueprint_group)


@app.get("/hello")
async def hello_app(_request: Request):
    """
    :param _request:
    :return:
    """
    return json({})


@app.exception(Exception)
async def handle_exception(request, exception):
    try:
        status_code = exception.status_code
    except:
        status_code = 400
    response = {
        "error": {
            "message": str(exception),
            "type": type(exception).__name__
        },
        "success": False,
        "meta_data": {},
    }
    return json(response, status=status_code)


if __name__ == "__main__":
    app.run(port=config.get("PORT"), auto_reload=True, access_log=True, debug=config.get("DEBUG"))
