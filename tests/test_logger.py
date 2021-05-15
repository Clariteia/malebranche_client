from malebranche.client import Malebranche


def test_logger():
    logger_instance = Malebranche("TestMicroservice", "localhost", 9343)

    with logger_instance.logger("INFO") as log:
        log.info("Testing")
        stack = log.stack
        assert stack[0]['level'] == "INFO"
