from io import (
    BytesIO,
)
from logging import (
    LogRecord,
)
from logging.handlers import (
    HTTPHandler,
)

from fastavro import (
    writer,
)

schema = {
    "name": "log_schema",
    "type": "record",
    "fields": [
        {"name": "message", "type": "string", "default": "Default"},
        {"name": "name", "type": "string"},
        {"name": "msg", "type": "string"},
        {"name": "name", "type": "string"},
        {"name": "args", "type": {"type": "array", "items": "string"}},
        {"name": "levelname", "type": "string"},
        {"name": "levelno", "type": "int"},
        {"name": "pathname", "type": "string"},
        {"name": "filename", "type": "string"},
        {"name": "module", "type": "string"},
        {"name": "exc_info", "type": "null"},
        {"name": "exc_text", "type": "null"},
        {"name": "stack_info", "type": "null"},
        {"name": "lineno", "type": "int"},
        {"name": "funcName", "type": "string"},
        {"name": "created", "type": "float"},
        {"name": "msecs", "type": "float"},
        {"name": "relativeCreated", "type": "float"},
        {"name": "thread", "type": "int"},
        {"name": "threadName", "type": "string"},
        {"name": "processName", "type": "string"},
        {"name": "process", "type": "string"},
        {"name": "parent", "type": "string", "default": "DEFAULT-PARENT"},
    ],
}


class HttpAvroHandler(HTTPHandler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def emit(self, record: LogRecord) -> None:
        try:
            import urllib.parse

            host = self.host
            h = self.getConnection(host, self.secure)
            url = self.url
            data = BytesIO()
            writer(data, schema, [self.mapLogRecord(record)])
            h.putrequest(self.method, url)

            if self.method == "POST":
                h.putheader("Content-type", "avro/binary")
                h.putheader("Content-length", str(len(data.getvalue())))

            h.endheaders()
            if self.method == "POST":
                h.send(data.getvalue())
            h.getresponse()  # can't do anything with the result
        except Exception as e:
            print(e)
