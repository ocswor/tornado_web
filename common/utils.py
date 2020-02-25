from main import Application


def request_wrap(route_path):
    def _deco(cls):
        Application.add_handlers(r".*", [(route_path, cls)])
        return cls

    return _deco
