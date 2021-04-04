import pandas
#import statistics

def load_data(path, features):
    df = pandas.read_csv(path, usecols=features)
    #print(df)
    data = df.to_dict(orient="list")
    # print(data)
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
    return data1


def print_details(data, features, statistic_functions):
    for key in features:
        begin = str(key) + ":"
        # for func in statistic_functions:
        # print(func(data[key]))
        print(begin, statistic_functions[0](data[key]), statistic_functions[1](data[key]), statistic_functions[2](data[key]))