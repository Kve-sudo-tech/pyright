from _typeshed import FileDescriptorOrPath
from pathlib import Path
from re import Pattern
from typing import IO, TypeVar
from typing_extensions import Self

from paramiko.message import Message

OPENSSH_AUTH_MAGIC: bytes

_BytesT = TypeVar("_BytesT", bound=bytes | bytearray)

def _unpad_openssh(data: _BytesT) -> _BytesT: ...

class PKey:
    public_blob: PublicBlob | None
    BEGIN_TAG: Pattern[str]
    END_TAG: Pattern[str]
    @staticmethod
    def from_path(path: Path | str, passphrase: bytes | None = None) -> PKey: ...
    @staticmethod
    def from_type_string(key_type: str, key_bytes: bytes) -> PKey: ...
    @classmethod
    def identifiers(cls) -> list[str]: ...
    def __init__(self, msg: Message | None = None, data: str | None = None) -> None: ...
    def asbytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def get_name(self) -> str: ...
    @property
    def algorithm_name(self) -> str: ...
    def get_bits(self) -> int: ...
    def can_sign(self) -> bool: ...
    def get_fingerprint(self) -> bytes: ...
    @property
    def fingerprint(self) -> str: ...
    def get_base64(self) -> str: ...
    def sign_ssh_data(self, data: bytes, algorithm: str | None = None) -> Message: ...
    def verify_ssh_sig(self, data: bytes, msg: Message) -> bool: ...
    @classmethod
    def from_private_key_file(cls, filename: FileDescriptorOrPath, password: str | None = None) -> Self: ...
    @classmethod
    def from_private_key(cls, file_obj: IO[str], password: str | None = None) -> Self: ...
    def write_private_key_file(self, filename: FileDescriptorOrPath, password: str | None = None) -> None: ...
    def write_private_key(self, file_obj: IO[str], password: str | None = None) -> None: ...
    def load_certificate(self, value: Message | str) -> None: ...

class PublicBlob:
    key_type: str
    key_blob: bytes
    comment: str
    def __init__(self, type_: str, blob: bytes, comment: str | None = None) -> None: ...
    @classmethod
    def from_file(cls, filename: FileDescriptorOrPath) -> Self: ...
    @classmethod
    def from_string(cls, string: str) -> Self: ...
    @classmethod
    def from_message(cls, message: Message) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
