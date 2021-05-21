from abc import ABC, abstractmethod


class ParserAbstract(ABC):
    __slots__ = "_type", "_stack", "_context"

    def __init__(self, context: "ContextManager", **kwargs):
        self._set_type()
        self._set_kwargs(kwargs)
        self._stack = []
        self._context = context

    @property
    def stack(self):
        return self._stack

    @abstractmethod
    def _set_type(self):
        raise NotImplemented

    def _set_kwargs(self, kwargs):
        pass

    def add_to_stack(self, **kwargs):
        """
        add the parameter passed by kwargs to a dictionary
        :param kwargs:
        :return:
        """
        data = {}
        data['type'] = self._type
        for key, value in kwargs.items():
            data[key] = value
        self._stack.append(data)
        self._context.add(data)
