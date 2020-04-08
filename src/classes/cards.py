from typing import Union, NewType
import numpy as np


CardSimple = NewType('CardSimple', np.bool)

_Card = NewType('_Card', Union[
    CardSimple
])