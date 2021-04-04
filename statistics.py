import math
from data import print_details


def sum(values):
    summary = 0
    for index in range(len(values)):
        summary += values[index]
    return summary


def mean(values):
    return float(sum(values)) / len(values)


def median(values):
    sorted_values = sorted(values)
    if len(sorted_values) % 2 == 0:
        return sorted_values[int(len(sorted_values) / 2 + 1)]
    return sorted_values[math.ceil(len(sorted_values) / 2)]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    data1 = {}
    for key in data.keys():
        data1[key] = []
    for index in range(len(data[treatment])):
        if(data[treatment][index] > threshold and is_above) or (data[treatment][index] <= threshold and not is_above):
            for key in data.keys():
                data1[key].append(data[key][index])

    print(feature_description)
    print_details(data1, target, statistic_functions)
