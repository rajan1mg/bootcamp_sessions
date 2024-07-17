from sanic import Blueprint

from app.routes.public.v1 import v1_blueprint

blueprint_group = Blueprint.group(v1_blueprint)
