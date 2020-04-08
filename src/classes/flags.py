from typing import Union, NewType


FlagSimple = NewType('FlagSimple', bool)

_Flag = NewType('_Flag', Union[
    FlagSimple
])