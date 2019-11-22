import os
import typing
import uuid

from utils.ThreadPool import ThreadPool


class Executor:
    def __init__(self, logger_folder: str, submit_folder: str, upload_folder: str) -> None:
        self.logger_folder: str = logger_folder
        self.submit_folder: str = submit_folder
        self.upload_folder: str = upload_folder

    def submit(self, json: typing.Dict[str, str]) -> typing.List[str]:
        try:
            ThreadPool.validate(json, ["script"])
            name: str = uuid.uuid4().get_hex()
            path: str = os.path.join(self.submit_folder, "{0}.bat".format(name))
            with open(path, "x") as file:
                file.write(json["script"])
            ThreadPool.submit(os.system, "{0} {1} > {2}".format(path, self.upload_folder, os.path.join(self.logger_folder, "{0}.log".format(name))))
            ThreadPool.submit(os.remove, path)
            return [name]
        except OSError:
            pass
        return []
