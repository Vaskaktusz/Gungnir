import os

from gungnir.utils.Blueprint import Blueprint
from gungnir.utils.LoginManager import LoginManager


class Logger(Blueprint):
    def init(self) -> None:
        os.makedirs(self.config["logger_folder"], exist_ok=True)

    def spec(self) -> None:
        pass


logger: Logger = Logger(LoginManager().system_loader)


@logger.route("/logger/<path:file>")
def _logger(file: str) -> str:
    return logger.flask.send_from_directory(logger.config["logger_folder"], file)


@logger.route("/loggers")
def _loggers() -> str:
    return logger.flask.json.dumps(os.listdir(logger.config["logger_folder"]))
