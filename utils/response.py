from sanic import json


def success(response, meta={}, status_code=200):
    return json(
        {"data": response,
         "success": True,
         "meta_data": meta
         }
        , status=status_code
    )
