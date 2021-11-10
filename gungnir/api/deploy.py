import os
import typing
import uuid

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager
from gungnir.utils.ThreadPool import ThreadPool


class Deploy(Blueprint):
    def detail(self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        return [{"rule": "/deploy", "endpoint": "_deploy", "view_func": _deploy, "methods": ["POST"]}]

    def launch(self) -> None:
        for folder in ["deploy", "logger", "upload"]:
            os.makedirs(os.path.join(deploy.config["bucket"], folder), exist_ok=True)


deploy: Deploy = Deploy(LoginManager().shadow_loader)


def _deploy() -> str:
    ThreadPool.verify(deploy.flask.request.json, ["script"])
    name: str = uuid.uuid4().hex
    path: str = os.path.join(deploy.config["bucket"], "deploy", name)
    with open(path, "x") as file:
        file.write(deploy.flask.request.json["script"])
    ThreadPool.submit(path, os.path.join(deploy.config["bucket"], "upload"), os.path.join(deploy.config["bucket"], "logger", name))
    return name
