"""
Class for Inner Ability Options
"""
import numpy as np


class ProbValOptions(object):
    """
    Options probability and corresponding values for inner ability.
    """

    def __init__(self, prob_tuple, val_tuple):
        self.__n_opt = len(prob_tuple)
        assert len(val_tuple) == len(prob_tuple)

        self.__val_tuple = val_tuple
        self.__cumsum_prob_tuple = tuple(np.cumsum(np.r_[0, prob_tuple]))

    def __get_idx(self, percentile):
        """
        Get the index from given percentile (0 - 99)
        that satisfies cumsum_prob[i] <= percentile < cumsum_prob[i+1]

        :param percentile: int, value in [0, 100)
        :return: idx: int, value in [0, n_opt)
        """
        opt_idx = np.searchsorted(self.__cumsum_prob_tuple, percentile, side='right')

        return opt_idx - 1

    def get_option_val(self, percentile):
        """
        Return the corresponding value given a percentile

        :param percentile: int, value in [0, 100)
        :return: opt_val
        """
        return self.__val_tuple[self.__get_idx(percentile)]

