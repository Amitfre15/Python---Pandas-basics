import pandas


def load_data(path, features):
    df = pandas.read_csv(path, usecols=features)
    data = df.to_dict(orient="list")
    return data


def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}
    for key in data.keys():
        data1[key] = []
        data2[key] = []
    for index in range(len(data[feature])):
        if data[feature][index] in values:
            for key in data.keys():
                data1[key].append(data[key][index])
        else:
            for key in data.keys():
                data2[key].append(data[key][index])
    return data1, data2


def print_details(data, features, statistic_functions):
    for key in features:
        print(key + ":", end=" ")
        for func in range(len(statistic_functions)):
            if func == len(statistic_functions)-1:
                print(statistic_functions[func](data[key]))
                continue
            print(statistic_functions[func](data[key]), end=", ")
