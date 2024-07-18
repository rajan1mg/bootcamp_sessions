import ujson


def json_file_to_dict(_file: str) -> dict:
    """

    :param _file:
    :return:
    """
    config = None
    try:
        with open(_file) as config_file:
            config = ujson.load(config_file)
    except (TypeError, FileNotFoundError, ValueError) as exception:
        print(exception)

    return config


class CONFIG:
    config = json_file_to_dict("./config.json")
