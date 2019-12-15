import typing

import flask

from gungnir.utils.Blueprint import Blueprint


class Flask(flask.Flask):
    def run(self, **options: typing.Union[str, typing.Dict[str, typing.Union[bool, int, str]], typing.List[Blueprint]]) -> None:
        url_config: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("url_config")
        url_prefix: str = options.pop("url_prefix")
        url_system: typing.Dict[str, typing.Union[bool, int, str]] = options.pop("url_system")
        urls: typing.List[Blueprint] = options.pop("urls")
        for url in urls:
            url.config = url_config
            url.mirror = urls
            url.system = url_system
            url.init()
            super().register_blueprint(url, url_prefix=url_prefix)
        super().run(**options)
