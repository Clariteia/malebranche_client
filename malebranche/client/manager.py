import uuid
from collections import deque


class ContextManager:
    __slots__ = "_process", "_id", "_parent_id", "_stack"

    def __init__(self):
        self._id = str(uuid.uuid1())
        self._parent_id = None
        self._process = deque()
        self._process.append(self._id)
        self._stack = []

    def add(self, data: dict):
        data['id_process'] = self._id
        if self._parent_id is not None:
            data['id_parent_process'] = self._parent_id
        print(f"Context data f{data}")
        self._stack.append(data)

    def add_child_process(self):
        self._parent_id = self._id
        self._id = str(uuid.uuid1())

