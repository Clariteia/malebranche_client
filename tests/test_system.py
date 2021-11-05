import httpretty

from malebranche.client.instance import (
    get_system,
)
from malebranche.client.parsers import (
    SystemParser,
)


@httpretty.activate
def test_system_values():
    stack = {}

    # def request_system_callback_response(request, uri, response_headers):
    #     request_dict = request.parsed_body
    #     assert request_dict["cpu_total"][0] == stack["cpu_total"], "Unexpected result"
    #     assert True == False, "the result is False and not True"
    #     return [200, response_headers, ""]
    #
    # httpretty.register_uri(httpretty.POST, "http://localhost:5000/system", body=request_system_callback_response)

    system = SystemParser(host="localhost:5000", url="/logs")
    stack = system.updateStack()
    system.emit()


# def test_context_system_values():
#     httpretty.enable(verbose=True, allow_net_connect=False)
#
#     def request_system_callback_response(request, uri, response_headers):
#         request_dict = request.parsed_body
#         return [200, response_headers, request_dict]
#
#     httpretty.register_uri(httpretty.POST, "http://localhost:5000/system",
#                            body=request_system_callback_response)
#     with get_system() as system:
#         print("this is a test")
#         response = system.emit()
#         print(response)
#
#     httpretty.disable()
#     httpretty.reset()
#     assert True == False
