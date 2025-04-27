from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListLobbiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLobbiesResponse(_message.Message):
    __slots__ = ("lobbies",)
    LOBBIES_FIELD_NUMBER: _ClassVar[int]
    lobbies: _containers.RepeatedCompositeFieldContainer[Lobby]
    def __init__(self, lobbies: _Optional[_Iterable[_Union[Lobby, _Mapping]]] = ...) -> None: ...

class Lobby(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
