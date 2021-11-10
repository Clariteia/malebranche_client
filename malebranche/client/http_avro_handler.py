from logging import LogRecord
from logging.handlers import HTTPHandler


class HttpAvroHandler(HTTPHandler):
    def emit(self, record: LogRecord) -> None:
        try:
            import urllib.parse

            host = self.host
            h = self.getConnection(host)
            url = self.url
            data = urllib.parse.urlencode(self.stack)
            h.putrequest(self.method, url)

            if self.method == "POST":
                h.putheader("Content-type", "application/x-www-form-urlencoded")
                h.putheader("Content-length", str(len(data)))

            h.endheaders()
            if self.method == "POST":
                h.send(data.encode("utf-8"))
            h.getresponse()  # can't do anything with the result
        except Exception as e:
            print(e)
