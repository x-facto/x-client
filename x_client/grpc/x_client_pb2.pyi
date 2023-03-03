from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NdArray(_message.Message):
    __slots__ = ["data", "dtype", "shape"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DTYPE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    dtype: str
    shape: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, dtype: _Optional[str] = ..., shape: _Optional[_Iterable[int]] = ..., data: _Optional[bytes] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["images"]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    images: _containers.RepeatedCompositeFieldContainer[NdArray]
    def __init__(self, images: _Optional[_Iterable[_Union[NdArray, _Mapping]]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["box", "pose"]
    BOX_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    box: _containers.RepeatedCompositeFieldContainer[NdArray]
    pose: _containers.RepeatedCompositeFieldContainer[NdArray]
    def __init__(self, box: _Optional[_Iterable[_Union[NdArray, _Mapping]]] = ..., pose: _Optional[_Iterable[_Union[NdArray, _Mapping]]] = ...) -> None: ...
