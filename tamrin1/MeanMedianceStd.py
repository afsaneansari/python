def median(ints):
    half = len(ints) / 2
    ints.sort()
    if len(ints) % 2 == 0:
        return (ints[half-1] + ints[half]) / 2.0
    else:
        return ints[half]

print median([1,2,3,5])


def mean(numberList):
    if len(numberList) == 0:
        return float('nan')

    floatNums = [float(x) for x in numberList]
    return sum(floatNums) / len(numberList)
print mean([1,2,3,4,5,6,7,8,9,10])

from math import sqrt
def mean_std_dev(durations):
    """ Calculate mean and standard deviation of data durations[]: """
    length, mean, std = len(durations), 0, 0
    for duration in durations:
        mean = mean + duration
    mean = mean / float(length)
    for duration in durations:
        std = std + (duration - mean) ** 2
    std = sqrt(std / float(length))
    mean = int(round(mean))
    std = int(round(std))
    return std

print mean_std_dev([1,2,3])