import base64
import pickle
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    left: Optional["Node"]
    right: Optional["Node"]
    value: Optional[str]
    frequency: int

    def __lt__(self, other: "Node"):
        return self.frequency < other.frequency


@dataclass
class EncodeResult:
    root: Node
    encoded_result: Optional[bytearray | str] = None
    length: Optional[int] = None


class DataSource:
    def write_result(self, result: EncodeResult, filepath: str):
        with open(filepath, "wb") as file:
            result.length = len(result.encoded_result)
            result.encoded_result = get_byte_array(
                result.encoded_result
            )

            pickle.dump(result, file)

    def write_file(self, text: str, filepath: str):
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)


    def read_file(self, filepath: str) -> str:
        with open(filepath, "r") as file:
            return file.read()


def get_byte_array(padded_encoded_text):
    while len(padded_encoded_text) % 8 != 0:
        padded_encoded_text += "0"
    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        b.append(int(byte, 2))
    return b


MEGABYTE = 1048576