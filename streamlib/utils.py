
def zeros(x_int):
    """
    @args
    x_int : an integer
    @return
    an integer, the # of trailing zeros in x_int (based on 2).
    if x_int == 0, return 0
    """
    ct = 0
    if x_int < 0: x_int = -x_int
    if x_int == 0: x_int = 1
    while not (x_int & 1):
        ct += 1
        x_int = (x_int >> 1) if x_int > 0 else 1
        
    return ct




# The following function copied from python3.4/Lib/statistics.py
def median(data):
    """Return the median (middle value) of numeric data.

    When the number of data points is odd, return the middle data point.
    When the number of data points is even, the median is interpolated by
    taking the average of the two middle values:

    >>> median([1, 3, 5])
    3
    >>> median([1, 3, 5, 7])
    4.0

    """
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise ValueError("no median for empty data")
    if n%2 == 1:
        return data[n//2]
    else:
        i = n//2
        return (data[i - 1] + data[i])/2



def CountBits(n):
    """ count # of 1 in a 64-bits number """
    n = (n & 0x5555555555555555) + ((n & 0xAAAAAAAAAAAAAAAA) >> 1)
    n = (n & 0x3333333333333333) + ((n & 0xCCCCCCCCCCCCCCCC) >> 2)
    n = (n & 0x0F0F0F0F0F0F0F0F) + ((n & 0xF0F0F0F0F0F0F0F0) >> 4)
    n = (n & 0x00FF00FF00FF00FF) + ((n & 0xFF00FF00FF00FF00) >> 8)
    n = (n & 0x0000FFFF0000FFFF) + ((n & 0xFFFF0000FFFF0000) >> 16)
    n = (n & 0x00000000FFFFFFFF) + ((n & 0xFFFFFFFF00000000) >> 32) # This last & isn't strictly necessary.
    return int(n)
