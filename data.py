import pandas


def load_data(path, features):
    """ Loads the supplied features from a csv file into a dataframe, converts it to a dictionary and returns it.

        :parameters:
        path -- csv file address
        features -- list of features to load from the file
        :returns: requested dictionary
    """
    df = pandas.read_csv(path, usecols=features)
    data = df.to_dict(orient="list")
    return data


def filter_by_feature(data, feature, values):
    """ Splits the dictionary to 2, one will hold only records in which the feature's value is included
        in the values list, the other will hold all the other records.

        :parameters:
        data -- a dictionary to filter
        feature -- the feature by which we'll filter
        values -- list of values to filter by (only those values will stay in the dictionary)
        :returns: both dictionaries
    """
    # declaration and initiation of empty dictionaries
    data1 = {}
    data2 = {}
    for key in data.keys():
        data1[key] = []
        data2[key] = []
    # iterating over the original records and splitting them according to their feature's value
    for index in range(len(data[feature])):
        if data[feature][index] in values:
            # copying a record to a new dictionary
            for key in data.keys():
                data1[key].append(data[key][index])
        else:
            for key in data.keys():
                data2[key].append(data[key][index])
    return data1, data2


def print_details(data, features, statistic_functions):
    """ Prints statistic values of supplied features from the dictionary

        :parameters:
        data -- the dictionary according to which the statistical values are determined
        features -- list of features to print their statistical values
        statistic_functions -- list of statistic functions in which we're interested
        :returns: None
    """
    for key in features:
        # Print each feature's values in one row
        print(key + ":", end=" ")
        for func in range(len(statistic_functions)):
            # When last function reached, move to a new row
            if func == len(statistic_functions)-1:
                print(statistic_functions[func](data[key]))
                continue
            print(statistic_functions[func](data[key]), end=", ")
