import os

import settings


class Settings(settings.Dict):
    def __init__(self, path: str) -> None:
        super().__init__(settings.settings[os.path.basename(path)])
