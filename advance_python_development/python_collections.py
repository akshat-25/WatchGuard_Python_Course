"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter

temp = [13.5,56.7,765.3]

temp_counter = Counter(temp)
print(temp_counter[56.7])

print(Counter({'hello' :5,'hi' : 4})['hi'])