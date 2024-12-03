##################################################
## load required packages ########################
##################################################

import numpy as np
import pandas as pd
from itertools import combinations

##################################################
## define function for solution A ################
##################################################

def safety_check(values):

    ## calculate differences between values on each line
    deltas =  np.diff(values)

    # determine consistency of sign and if differences are within range
    consistent_sign = all(np.array(deltas) < 0) or all(np.array(deltas) > 0)
    diffs_within_range = all(abs(deltas) >= 1) and all(abs(deltas) <= 3)

    ## specify final result
    safety_pass = consistent_sign and diffs_within_range

    ## create dictionary with results
    ## this was for exploring, but not actually needed
    data = {
        "Values": [values],
        "Deltas": [deltas.tolist()],
        "Consistent Sign": [consistent_sign],
        "Diffs Within Range": [diffs_within_range],
        "Safety Pass": [safety_pass]
    }

    return(safety_pass)

##################################################
## define function for solution B ################
##################################################

# original solution
#def safety_check_with_deletion(values):
#    return safety_check(values) or any(safety_check(values[:i] + values[i+1:]) for i in range(len(values)))

# with itertools
def safety_check_with_deletion(values):
    return safety_check(values) or any(safety_check(subvalues) for subvalues in combinations(values, len(values) - 1))

##################################################
## read in data and apply functions ##############
##################################################

with open("02-input.txt") as file:
    rows = [list(map(int, line.split())) for line in file]
    print(f"Safe (solution A): {sum(safety_check(r) for r in rows)}")
    print(f"Safe (solution B): {sum(safety_check_with_deletion(r) for r in rows)}")
