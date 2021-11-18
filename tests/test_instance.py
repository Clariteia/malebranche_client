import httpretty

from malebranche.client.instance import start_span


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

    with start_span() as span:
        span.logger.info("First")
        with start_span() as sub_span:
            sub_span.logger.info("Second")
            with start_span() as sub_sub_span:
                sub_sub_span.logger.info("Third")
            sub_span.logger.info("Sub-Second")
        span.logger.info("Sub-First")


def test_simple():
    with start_span() as span:
        span.logger.info("Hello, world!")
