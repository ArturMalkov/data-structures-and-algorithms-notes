"""
Amortized Constant Performance of Method

Amortized constant O(1):
- means that given sufficient number of requests, the average performance time is constant;
- occasionally one operation could require O(n) in the worst case (when some internal bookkeeping takes place).

Most frequently occurs with hashing whose performance depends on statistical estimates.

May happen when appending to a list fills the list to the end and requires allocation of more space.
May occur when garbage collection algorithms routinely go through and free up memory - you never know when that's going
to happen.
"""