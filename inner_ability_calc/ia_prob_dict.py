"""
Inner ability probability dictionary

Reference: https://maplestory.nexon.com/Guide/OtherProbability/ability/reputevalue

NOTES
-----
1. Only useful ones are listed.
2. The number is percentage (e.g. 2.22 = 2.22% chance)
"""
import numpy as np
from collections import namedtuple

LEG_PROB_DICT = {
    'att': 2.22,
    'matt': 2.22,
    'crit': 0.44,
    'att_spd': 0.44,
    'boss': 2.22,
    'mob': 1.78,
    'abnormal': 1.78,
    'skip_cd': 1.78,
    'buff': 0.89,
    'item': 1.78,
    'meso': 1.78
}

UNIQ_PROB_DICT = {
    'att': 1.29,
    'matt': 1.29,
    'crit': 0.43,
    'boss': 0.86,
    'mob': 1.72,
    'abnormal': 1.72,
    'skip_cd': 1.72,
    'buff': 0.86,
    'item': 1.72,
    'meso': 1.72
}


class IAOptions(object):
    """
    Options chance and values for inner ability.

    TODO: Currently only unique and legendary are recorded.
    """
    IA_OPTION_PROB_TUPLE = (20, 20, 20, 15, 15, 10)

    def __init__(self, uniq_val_tuple, legend_val_tuple):
        self.__n_opt = len(self.IA_OPTION_PROB_TUPLE)
        assert len(uniq_val_tuple) == self.__n_opt
        assert len(legend_val_tuple) == self.__n_opt

        self.__uniq_val_tuple = uniq_val_tuple
        self.__legend_val_tuple = legend_val_tuple

        self.__cumsum_prob_tuple = tuple(np.cumsum(np.r_[0, self.IA_OPTION_PROB_TUPLE]))

    def __get_idx(self, percentile):
        """
        Get the index from given percentile (0 - 99)
        that satisfies cumsum_prob[i] <= percentile < cumsum_prob[i+1]

        :param percentile: int, value in [0, 100)
        :return: idx: int, value in [0, n_opt)
        """
        opt_idx = self.__cumsum_prob_tuple.searchsorted(percentile, side='right')

        return opt_idx - 1

    def get_uniq_option(self, percentile):
        """
        Return the corresponding unique value given a percentile
        :return:
        """
        return self.__uniq_val_tuple[self.__get_idx(percentile)]

    def get_legend_option(self, percentile):
        """
        Return the corresponding legendary value given a percentile
        :return:
        """
        return self.__legend_val_tuple[self.__get_idx(percentile)]

IAOptions = namedtuple('IAOptions', ['uniq', 'legend'])
IA_OPTION_VAL_DICT = {
    'att': IAOptions()
}