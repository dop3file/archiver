import heapq
from collections import Counter
from typing import Optional

from utils import Node, EncodeResult


class HuffmanEncoder:
    def get_symbols_frequency(self, text: str) -> dict[str, int]:
        result = Counter(text)
        return result

    def build_tree(self, text: str):
        queue = [
            Node(value=key, frequency=value, left=None, right=None) for (key, value) in self.get_symbols_frequency(text).items()
        ]
        heapq.heapify(queue)

        while len(queue) > 1:
            left = heapq.heappop(queue)
            right = heapq.heappop(queue)
            new_node = Node(
                left=left,
                right=right,
                frequency=left.frequency + right.frequency,
                value=None
            )
            heapq.heappush(queue, new_node)

        root = queue[0]
        return root

    def get_codes_wrapper(self, root: Optional[Node], current_code: str, codes: dict):
        if root is None:
            return

        if root.value is not None:
            codes[root.value] = current_code
            return
        self.get_codes_wrapper(root.left, current_code + "0", codes)
        self.get_codes_wrapper(root.right, current_code + "1", codes)

    def get_codes(self, text: str) -> str:
        result = ""
        codes = {}
        self.get_codes_wrapper(
            self.build_tree(text),
            "",
            codes
        )
        for ch in text:
            result += codes[ch]
        return result

    def encode(self, text: str) -> EncodeResult:
        return EncodeResult(root=self.build_tree(text), encoded_result=self.get_codes(text))



