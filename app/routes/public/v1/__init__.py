from sanic import Blueprint

from app.routes.public.v1.user import user_bp

v1_blueprint = Blueprint.group(user_bp, url_prefix='/v1')
