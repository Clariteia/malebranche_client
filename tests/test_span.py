from time import (
    sleep,
)

import httpretty

from malebranche.client import (
    Span,
)


@httpretty.activate
def test_logger_multi_context():
    message = {}

    def request_callback_response(request, uri, response_headers):
        request_dict = request.parsed_body
        message[request_dict["msg"][0]] = {}
        message[request_dict["msg"][0]]["process"] = request_dict["process"][0]
        if "parent" in request_dict:
            message[request_dict["msg"][0]]["parent"] = request_dict["parent"][0]
        if request_dict["msg"][0] == "Second":
            assert message["First"]["process"] == request_dict["parent"][0]
        return [200, response_headers, ""]

    httpretty.register_uri(httpretty.POST, "http://localhost:5000/logs", body=request_callback_response)

    with Span() as span:
        span.logger.info("First")
        with Span() as sub_span:
            sub_span.logger.info("Second")
            with Span() as sub_sub_span:
                sub_sub_span.logger.info("Third")
            sub_span.logger.info("Sub-Second")
        span.logger.info("Sub-First")


def test_simple():
    with Span() as span:
        span.logger.info("Hello, world!")


def test_playground():
    with Span() as span:

        def a():
            print(999998 in d)

        def b():
            print(999998 in l)

        d = {i: i for i in range(999999)}
        l = [i for i in range(999999)]
        a()
        b()