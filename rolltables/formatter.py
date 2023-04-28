import string
from typing import List


class _Formatter(string.Formatter):
    def get_field_names(self, format_string: str) -> List[str]:
        return [i[1] for i in self.parse(format_string) if i[1] is not None]

    def _vformat(self, format_string, args, kwargs, used_args, recursion_depth, auto_arg_index=0):
        if recursion_depth < 0:
            raise ValueError("Max string recursion exceeded")

        result = []
        for literal_text, field_name, format_spec, conversion in self.parse(format_string):
            # output the literal text
            if literal_text:
                result.append(literal_text)

            # if there's a field, output it
            if field_name is not None:
                field_name = str(auto_arg_index)
                auto_arg_index += 1

                # given the field_name, find the object it references
                #  and the argument it came from
                obj, arg_used = self.get_field(field_name, args, kwargs)
                used_args.add(arg_used)

                # do any conversion on the resulting object
                obj = self.convert_field(obj, conversion)

                # expand the format spec, if needed
                format_spec, auto_arg_index = self._vformat(
                    format_spec,
                    args,
                    kwargs,
                    used_args,
                    recursion_depth - 1,
                    auto_arg_index=auto_arg_index,
                )

                # format the object and append to the result
                result.append(self.format_field(obj, format_spec))

        return "".join(result), auto_arg_index


Formatter = _Formatter()
