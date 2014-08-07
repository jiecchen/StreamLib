
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
