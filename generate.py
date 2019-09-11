# @author Anton Hrytsyk
# This script computes the histogram of nums against the bins.

import matplotlib.pyplot as mp
import numpy as np

bins = np.array([0, 1, 2, 3])
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])

print("This script computes the histogram of nums against the bins.")
print("nums: ", nums)
print("bins: ", bins)
print("results: ", np.histogram(nums, bins))

mp.hist(nums, bins=bins)
mp.show()
