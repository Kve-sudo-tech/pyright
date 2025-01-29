from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

@_dispatchable
def from_graph6_bytes(bytes_in): ...
def to_graph6_bytes(G, nodes: Incomplete | None = None, header: bool = True): ...
@_dispatchable
def read_graph6(path): ...
def write_graph6(G, path, nodes: Incomplete | None = None, header: bool = True): ...
