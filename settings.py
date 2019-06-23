import typing

settings: typing.Dict[str, typing.Dict[str, typing.Union[bool, int, str]]] = {
    "wsdl": {
        "debug": False,
        "host": "0.0.0.0",
        "port": 5000,
    },
    "logger.py": {
        "folder": "logger"
    }
}
