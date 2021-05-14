class Malebranche(object):
    __slots__ = "_host", "_port", "_service_name"

    def __init__(self, service_name: str, host: str, port: int):
        self._host = host
        self._port = port
        self._service_name = service_name
        
    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()
