from typing import List

class Loader():

    def __init__(self) -> None:
        pass

    def load_data(first, file: str) -> List[str]:
        with open(file) as f:
            content = [line.rstrip() for line in f]
        return content