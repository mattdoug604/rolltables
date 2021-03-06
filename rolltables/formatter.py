import string
from typing import List


class _Formatter(string.Formatter):
    def get_field_names(self, format_string: str) -> List[str]:
        return [i[1] for i in self.parse(format_string) if i[1] is not None]


Formatter = _Formatter()
