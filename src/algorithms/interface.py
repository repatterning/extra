"""Module interface.py"""
import logging

import pandas as pd

import config
import src.algorithms.algorithm
import src.algorithms.points


class Interface:
    """
    The model building steps vis-à-vis a Bayesian Vector Autoregressive Algorithm
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

        # The variables
        self.__columns = ['value', 'catchment_size', 'gauge_datum']

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d\n',
                            datefmt='%Y-%m-%d %H:%M:%S')

        self.__logger = logging.getLogger(__name__)

    def exc(self):
        """

        :return:
        """

        points: pd.DataFrame = src.algorithms.points.Points().exc()
        points.info()

        frame: pd.DataFrame = points.copy().loc[points['timestamp'] < self.__configurations.cutoff, :]
        frame.sort_values(by=['station_id', 'timestamp'], ascending=True, inplace=True)
        frame.info()

        algorithm = src.algorithms.algorithm.Algorithm()
        model, i_data = algorithm.exc(n_lags=2, frame=frame, columns=self.__columns, groupings='station_id', _priors=False)

        self.__logger.info(model)
        self.__logger.info(i_data)
