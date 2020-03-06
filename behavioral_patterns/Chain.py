class Handler:

    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            print(f"{self._name} can not handle request {request}. Maybe {self._successor._name} can...")
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass!")

    @property
    def _name(*args, **kwargs):
        return 'placeholder'


class ConcreteHandler1(Handler):

    def _handle(self, request):
        if 0 < request <= 10:
            print(f"Request {request} handled by {self._name}")
            return True

    @property
    def _name(*args, **kwargs):
        return 'Handler 1'


class ConcreteHandler2(Handler):

    def _handle(self, request):
        if 10 < request <= 20:
            print(f"Request {request} handled by {self._name}")
            return True

    @property
    def _name(*args, **kwargs):
        return 'Handler 2'


class DefaultHandler(Handler):

    def _handle(self, request):
        print(f"End chain - no handler for request {request}")
        return True

    @property
    def _name(*args, **kwargs):
        return 'Default Handler'


class Client:

    def __init__(self):
        self.handler = ConcreteHandler1(
                            ConcreteHandler2(
                                DefaultHandler(None)
                            )
                        )

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


c = Client()

requests = [2, 5, 19, 30]

c.delegate(requests)
