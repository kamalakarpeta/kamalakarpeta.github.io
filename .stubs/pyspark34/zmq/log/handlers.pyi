import logging
import zmq
from _typeshed import Incomplete

TOPIC_DELIM: str

class PUBHandler(logging.Handler):
    '''A basic logging handler that emits log messages through a PUB socket.

    Takes a PUB socket already bound to interfaces or an interface to bind to.

    Example::

        sock = context.socket(zmq.PUB)
        sock.bind(\'inproc://log\')
        handler = PUBHandler(sock)

    Or::

        handler = PUBHandler(\'inproc://loc\')

    These are equivalent.

    Log messages handled by this handler are broadcast with ZMQ topics
    ``this.root_topic`` comes first, followed by the log level
    (DEBUG,INFO,etc.), followed by any additional subtopics specified in the
    message by: log.debug("subtopic.subsub::the real message")
    '''
    ctx: zmq.Context
    socket: zmq.Socket
    formatters: Incomplete
    def __init__(self, interface_or_socket: str | zmq.Socket, context: zmq.Context | None = None, root_topic: str = '') -> None: ...
    @property
    def root_topic(self) -> str: ...
    @root_topic.setter
    def root_topic(self, value: str): ...
    def setRootTopic(self, root_topic: str):
        """Set the root topic for this handler.

        This value is prepended to all messages published by this handler, and it
        defaults to the empty string ''. When you subscribe to this socket, you must
        set your subscription to an empty string, or to at least the first letter of
        the binary representation of this string to ensure you receive any messages
        from this handler.

        If you use the default empty string root topic, messages will begin with
        the binary representation of the log level string (INFO, WARN, etc.).
        Note that ZMQ SUB sockets can have multiple subscriptions.
        """
    def setFormatter(self, fmt, level=...) -> None:
        """Set the Formatter for this handler.

        If no level is provided, the same format is used for all levels. This
        will overwrite all selective formatters set in the object constructor.
        """
    def format(self, record):
        """Format a record."""
    def emit(self, record) -> None:
        """Emit a log message on my socket."""

class TopicLogger(logging.Logger):
    """A simple wrapper that takes an additional argument to log methods.

    All the regular methods exist, but instead of one msg argument, two
    arguments: topic, msg are passed.

    That is::

        logger.debug('msg')

    Would become::

        logger.debug('topic.sub', 'msg')
    """
    def log(self, level, topic, msg, *args, **kwargs) -> None:
        '''Log \'msg % args\' with level and topic.

        To pass exception information, use the keyword argument exc_info
        with a True value::

            logger.log(level, "zmq.fun", "We have a %s",
                    "mysterious problem", exc_info=1)
        '''

meth: Incomplete
