from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Visual(Blueprint):
    def init(self) -> None:
        pass


visual: Visual = Visual(LoginManager().vacant_loader)


@visual.route("/")
def _visual() -> str:
    return visual.flask.render_template("visual.html", **visual.system)
