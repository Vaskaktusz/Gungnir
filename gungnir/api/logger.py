import flask

from util.Settings import Settings

logger: flask.Blueprint = flask.Blueprint("logger", __name__)
settings: Settings = Settings(__file__)


@logger.route("/loggers")
def _loggers() -> str:
    return flask.json.dumps([])


@logger.route("/logger/<id>")
def _logger(id: str) -> str:
    return ""
