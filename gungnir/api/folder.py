import os
import typing

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Folder(Blueprint):
    def detail(self) -> typing.List[typing.Dict[str, typing.Union[str, typing.Callable[..., str], typing.List[str]]]]:
        return [
            {"rule": "/folders/<path>/<file>", "endpoint": "_delete_file", "view_func": _delete_file, "methods": ["DELETE"]},
            {"rule": "/folders/<path>/<file>", "endpoint": "_file", "view_func": _file, "methods": ["GET"]},
            {"rule": "/folders/<path>", "endpoint": "_files", "view_func": _files, "methods": ["GET"]},
            {"rule": "/folders/<path>", "endpoint": "_post_file", "view_func": _post_file, "methods": ["POST"]}
        ]


folder: Folder = Folder(LoginManager().shadow_loader)


def _delete_file(path: str, file: str) -> str:
    os.remove(os.path.join(folder.config["folder"], path, file))
    return ""


def _file(path: str, file: str) -> str:
    return folder.flask.send_from_directory(os.path.join(folder.config["folder"], path), file)


def _files(path: str) -> str:
    result: typing.Dict[str, typing.Dict[str, int]] = {}
    for file in os.scandir(os.path.join(folder.config["folder"], path)):
        result[file.name] = dict(zip(("mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"), file.stat()))
    return folder.flask.json.dumps(result)


def _post_file(path: str) -> str:
    for file in folder.flask.request.files:
        try:
            file.save(os.path.join(folder.config["folder"], path, folder.werkzeug.utils.secure_filename(file)))
        except FileNotFoundError:
            os.makedirs(os.path.join(folder.config["folder"], path))
            return _post_file(path)
    return ""