from _typeshed import Incomplete

class EventListenerStub:
    """EventListener: Receives Event protos, e.g., from debugged TensorFlow
    runtime(s).
    """
    SendEvents: Incomplete
    SendTracebacks: Incomplete
    SendSourceFiles: Incomplete
    def __init__(self, channel) -> None:
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class EventListenerServicer:
    """EventListener: Receives Event protos, e.g., from debugged TensorFlow
    runtime(s).
    """
    def SendEvents(self, request_iterator, context) -> None:
        """Client(s) can use this RPC method to send the EventListener Event protos.
        The Event protos can hold information such as:
        1) intermediate tensors from a debugged graph being executed, which can
        be sent from DebugIdentity ops configured with grpc URLs.
        2) GraphDefs of partition graphs, which can be sent from special debug
        ops that get executed immediately after the beginning of the graph
        execution.
        """
    def SendTracebacks(self, request, context) -> None:
        """Send the tracebacks of a TensorFlow execution call.
        """
    def SendSourceFiles(self, request, context) -> None:
        """Send a collection of source code files being debugged.
        """

def add_EventListenerServicer_to_server(servicer, server) -> None: ...

class EventListener:
    """EventListener: Receives Event protos, e.g., from debugged TensorFlow
    runtime(s).
    """
    @staticmethod
    def SendEvents(request_iterator, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def SendTracebacks(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
    @staticmethod
    def SendSourceFiles(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
