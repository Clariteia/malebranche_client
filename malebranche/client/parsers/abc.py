import abc


class HttpStreamParser(abc.ABC):
    __slots__ = "host", "url", "method", "stack"

    def __init__(self, host, url, method="POST"):
        """
        Initialize the instance with the host, the request URL, and the method
        ("GET" or "POST")
        """
        method = method.upper()
        self.host = host
        self.url = url
        self.method = method
        self.stack = {}

    def getConnection(self, host):
        """
        get a HTTP[S]Connection.

        Override when a custom connection is required, for example if
        there is a proxy.
        """
        import http.client

        connection = http.client.HTTPConnection(host)
        return connection

    @abc.abstractmethod
    def updateStack(self):
        raise NotImplementedError

    def emit(self):
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
