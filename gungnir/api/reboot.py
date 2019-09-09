from services.Housekeeper import Housekeeper
from utils.Blueprint import Blueprint
from utils.LoginManager import LoginManager


class Reboot(Blueprint):
    def init(self) -> None:
        pass


reboot: Reboot = Reboot(LoginManager().ba_spwd)


@reboot.route("/reboot", methods=["POST"])
def _reboot() -> str:
    raise NotImplementedError()


@reboot.route("/remove", methods=["POST"])
def _remove() -> str:
    return reboot.flask.json.dumps(Housekeeper(
        reboot.settings["submit_folder"],
        reboot.settings["submit_folder"]).remove(reboot.flask.request.json))
