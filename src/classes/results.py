from typing import Union, NewType
import numpy as np
import pandas as pd


ResultsOfGameSimple = NewType('ResultsOfGameSimple', np.ndarray)

_ResultsOfGame = NewType('_ResultsOfGame', Union[
    ResultsOfGameSimple
])


ResultsOfEvaluatorSimple = NewType('ResultsOfEvaluatorSimple', pd.DataFrame)

_ResultsOfEvaluator = NewType('_ResultsOfEvaluator', Union[
    ResultsOfEvaluatorSimple
])