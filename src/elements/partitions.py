"""Module partitions.py"""
import typing

import numpy as np


class Partitions(typing.NamedTuple):
    """
    The data type class ⇾ Partitions<br><br>

    Attributes<br>
    ----------<br>
    ts_id: int<br>

    period: str<br>

    catchment_size: float<br>

    gauge_datum: float<br>
        The elevation above ...<br>
    on_river: bool<br>

    """

    ts_id: int
    period: str
    catchment_size: float
    gauge_datum: float
    on_river: bool
