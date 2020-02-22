import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Device(Blueprint):
    def detail(self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        return [
            {"rule": "/device", "endpoint": "_device", "view_func": _device, "methods": ["GET"]},
            {"rule": "/health", "endpoint": "_health", "view_func": _health, "methods": ["GET"]}
        ]

    def enable(self) -> None:
        pass


device: Device = Device(LoginManager().shadow_loader)


def _device() -> str:
    return device.flask.json.dumps(dict(zip(("sysname", "nodename", "release", "version", "machine"), os.uname())))


def _health() -> str:
    return ""
