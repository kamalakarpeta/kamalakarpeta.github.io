from _typeshed import Incomplete

__all__ = ['weakref_finalize']

class weakref_finalize:
    """Class for finalization of weakrefable objects
    finalize(obj, func, *args, **kwargs) returns a callable finalizer
    object which will be called when obj is garbage collected. The
    first time the finalizer is called it evaluates func(*arg, **kwargs)
    and returns the result. After this the finalizer is dead, and
    calling it just returns None.
    When the program exits any remaining finalizers for which the
    atexit attribute is true will be run in reverse order of creation.
    By default atexit is true.
    """
    class _Info: ...
    def __init__(self, obj, func, *args, **kwargs) -> None: ...
    def __call__(self, _: Incomplete | None = None):
        """If alive then mark as dead and return func(*args, **kwargs);
        otherwise return None"""
    def detach(self):
        """If alive then mark as dead and return (obj, func, args, kwargs);
        otherwise return None"""
    def peek(self):
        """If alive then return (obj, func, args, kwargs);
        otherwise return None"""
    @property
    def alive(self):
        """Whether finalizer is alive"""
    @property
    def atexit(self):
        """Whether finalizer should be called at exit"""
    @atexit.setter
    def atexit(self, value) -> None: ...
