import uuid
from collections import (
    deque,
)


class ContextManager:
    __slots__ = "_process", "_stack"

    def __init__(self):
        self._process = deque()
        self._process.append({"process": str(uuid.uuid1()), "parent": None})
        self._stack = []

    @property
    def process(self):
        return self._process[-1]

    def add(self, data: dict):
        actual_process = self._process[-1]
        data["id_process"] = actual_process["process"]
        if actual_process["parent"] is not None:
            data["id_parent_process"] = actual_process["parent"]
        self._stack.append(data)

    def add_child_process(self):
        actual_process = self._process[-1]
        self._process.append({"process": str(uuid.uuid1()), "parent": actual_process["process"]})

    def remove_child(self):
        self._process.pop()
