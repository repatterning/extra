
import pandas as pd

import src.elements.specifications as se


class Specifications:

    def __init__(self):
        pass

    @staticmethod
    def exc(reference: pd.DataFrame) -> list[se.Specifications]:

        dictionaries = [reference.iloc[i, :].squeeze() for i in range(reference.shape[0])]
        specifications = [se.Specifications(**dictionary) for dictionary in dictionaries]

        return specifications
