import base64
import crypt
import os
import spwd
import sys
import typing


class LoginManager:
    def shadow_loader(self, headers: typing.Dict[str, str]) -> None:
        try:
            getattr(self, "_shadow_{0}".format(sys.platform))(*base64.b64decode(headers.get("Authorization").replace("Basic ", "", 1)).decode().split(":"))
        except (AttributeError, TypeError, ValueError):
            raise PermissionError()

    def vacant_loader(self, headers: typing.Dict[str, str]) -> None:
        pass

    def _shadow_linux(self, username: str, password: str) -> None:
        sp_namp: str = os.getlogin()
        sp_pwdp: str = spwd.getspnam(sp_namp).sp_pwdp
        if sp_namp.__ne__(username) or sp_pwdp.__ne__(crypt.crypt(password, sp_pwdp)):
            raise PermissionError()
