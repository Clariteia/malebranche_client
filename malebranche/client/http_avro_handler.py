from io import BytesIO
from logging import LogRecord
from logging.handlers import HTTPHandler

from fastavro import writer

schema = {
    'name': 'log_schema',
    'type': 'record',
    'fields': [
        {'name': 'message', 'type': 'string'},
        {'name': 'name', 'type': 'string'},
        {'name': 'msg', 'type': 'string'},
        {'name': 'name', 'type': 'string'},
        {'name': 'args', 'type': 'string'},
        {'name': 'levelname', 'type': 'string'},
        {'name': 'levelno', 'type': 'string'},
        {'name': 'pathname', 'type': 'string'},
        {'name': 'filename', 'type': 'string'},
        {'name': 'module', 'type': 'string'},
        {'name': 'exc_info', 'type': 'string'},
        {'name': 'exc_text', 'type': 'string'},
        {'name': 'stack_info', 'type': 'string'},
        {'name': 'lineno', 'type': 'string'},
        {'name': 'funcName', 'type': 'string'},
        {'name': 'created', 'type': 'string'},
        {'name': 'msecs', 'type': 'string'},
        {'name': 'relativeCreated', 'type': 'string'},
        {'name': 'thread', 'type': 'string'},
        {'name': 'threadName', 'type': 'string'},
        {'name': 'processName', 'type': 'string'},
        {'name': 'process', 'type': 'string'},
        {'name': 'parent', 'type': 'string'},
    ],
}


class HttpAvroHandler(HTTPHandler):
    def emit(self, record: LogRecord) -> None:
        try:
            import urllib.parse

            host = self.host
            h = self.getConnection(host, self.secure)
            url = self.url
            data = BytesIO()
            writer(data, schema, self.mapLogRecord(record))
            h.putrequest(self.method, url)

            if self.method == "POST":
                h.putheader("Content-type", "avro/binary")
                h.putheader("Content-length", str(len(data)))

            h.endheaders()
            if self.method == "POST":
                h.send(data.encode("utf-8"))
            h.getresponse()  # can't do anything with the result
        except Exception as e:
            print(e)
