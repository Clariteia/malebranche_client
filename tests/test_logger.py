from malebranche.client.instance import (
    get_logger,
)

# def test_logger_string_message():
#     with get_logger() as log:
#         log.info("Testing")


# def test_logger_int_message():
#     with get_logger() as log:
#         log.info(12)
#         list_messages = log.stack
#         assert list_messages[0]["body"] == 12
#
#
# def test_logger_dict_message():
#     with get_logger() as log:
#         log.info({"name": "malebranche"})
#         list_messages = log.stack
#         assert list_messages[0]["body"]["name"] == "malebranche"
#
#
# def test_logger_list_message():
#     with get_logger() as log:
#         log.info(["malebranche"])
#         list_messages = log.stack
#     assert list_messages[0]["body"][0] == "malebranche"
#
#
def test_multi_logger_context():
    with get_logger() as log:
        log.info("Test: first process")
        with get_logger() as sub_log:
            sub_log.warning("Test: Warning sub process")
            with get_logger() as sub_sub_log:
                sub_sub_log.debug("Test: Debug sub sub process")
            sub_log.info("Test: Info sub process after")
        log.debug("Test: Debug process message")
