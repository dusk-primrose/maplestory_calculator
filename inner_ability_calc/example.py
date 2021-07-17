"""
Example module to run Inner Ability calculator
"""
import numpy as np
from ia_calc import IALine, IARollUniqLine, IARollLegendLine, IARollOneLineCount
from ia_calc import SecThirdLineRankRoll


req_line = IALine('Unique', 'buff', 38)
ia_roll_uniq_line = IARollUniqLine()
sec_third_line_rank_roll = SecThirdLineRankRoll()

np.random.seed(50)

n_count_list = [IARollOneLineCount.get_count(req_line, sec_third_line_rank_roll, ia_roll_uniq_line, []) for _ in range(100)]

print(np.mean(n_count_list))
print(np.percentile(n_count_list, [5, 25, 50, 75, 95]))

