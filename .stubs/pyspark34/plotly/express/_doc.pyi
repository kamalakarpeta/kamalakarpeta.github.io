import inspect
from _typeshed import Incomplete

getfullargspec = inspect.getfullargspec
getfullargspec = inspect.getargspec
colref_type: str
colref_desc: str
colref_list_type: str
colref_list_desc: str
docs: Incomplete

def make_docstring(fn, override_dict: Incomplete | None = None, append_dict: Incomplete | None = None): ...
