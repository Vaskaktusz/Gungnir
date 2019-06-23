import os

from util.Blueprint import Blueprint


class Logger(Blueprint):
    def init(self) -> None:
        if not os.path.exists(self.settings["folder"]):
            os.makedirs(self.settings["folder"])


logger: Logger = Logger(__file__, __name__)


@logger.route("/loggers")
def _loggers() -> str:
    return logger.flask.json.dumps(os.listdir(logger.settings["folder"]))


@logger.route("/logger/<path:filename>")
def _logger(filename: str) -> str:
    return logger.flask.send_from_directory(logger.settings["folder"], filename)
