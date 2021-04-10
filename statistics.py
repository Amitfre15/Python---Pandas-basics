from data import print_details


def sum(values):
    """Return the summary of the values list.  """
    summary = 0
    for index in range(len(values)):
        summary += values[index]
    return summary


def mean(values):
    """Return the mean value of the values list."""
    return float(sum(values)) / len(values)


def median(values):
    """Return the median value of the values list."""
    sorted_values = sorted(values)
    if len(sorted_values) % 2 == 0:
        return float((sorted_values[int(len(sorted_values) / 2) - 1] + sorted_values[int(len(sorted_values) / 2)]) / 2)
    return float(sorted_values[int(len(sorted_values) / 2)])


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """ Filters the dictionary to hold only records in which the treatment feature's value is above/equal or below
        the threshold supplied (according to is_above argument value).
        Prints statistic values of the target feature from the filtered dictionary.

        :parameters:
        feature_description -- a description of the records in data
        data -- the dictionary to filter from
        treatment -- a feature to filter by
        target -- a feature according to which we'll print the statistic values
        threshold -- a value to filter treatment's values by
        is_above -- boolean, determines whether to filter the values above threshold the opposite
        statistic_functions -- list of statistic functions in which we're interested
        :returns: None
    """
    data1 = {}
    for key in data.keys():
        data1[key] = []
    for index in range(len(data[treatment])):
        if(data[treatment][index] > threshold and is_above) or (data[treatment][index] <= threshold and not is_above):
            # copying a record to a new dictionary
            for key in data.keys():
                data1[key].append(data[key][index])

    print(feature_description)
    print_details(data1, target, statistic_functions)
