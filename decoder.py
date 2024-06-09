import pickle

from bitarray import bitarray

from utils import EncodeResult


class HuffmanDecoder:
    def get_text_from_result(self, encoded_result: EncodeResult) -> bitarray:
        text = bitarray()
        text.frombytes(encoded_result.encoded_result)
        return text[:encoded_result.length]

    def decode(self, encoded_result: EncodeResult):
        text = self.get_text_from_result(encoded_result)
        tmp = encoded_result.root
        result = ""
        for ch in text:
            if str(ch) == "0":
                tmp = tmp.left
            else:
                tmp = tmp.right
            if tmp.left is None and tmp.right is None:
                result += tmp.value
                tmp = encoded_result.root
        return result

    def read(self, filepath: str) -> EncodeResult:
        with open(filepath, 'rb') as file:
            obj = pickle.load(file)
        return obj
