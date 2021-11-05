import httpretty

from malebranche.client.instance import (
    get_logger,
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

    httpretty.register_uri(httpretty.POST, "http://localhost:5000/log", body=request_callback_response)

    with get_logger() as log:
        log.info("First")
        with get_logger() as sub_log:
            sub_log.warning("Second")
            with get_logger() as sub_sub_log:
                sub_sub_log.debug("Third")
            sub_log.info("Sub-Second")
        log.debug("Sub-First")


def test_logger():
    with get_logger() as log:
        log.info("First")
        with get_logger() as sub_log:
            sub_log.warning("Second")
