import sys
import pandas
import data
import statistics

def main(argv):
    features = (argv[2].split(sep=", "))
    the_data = data.load_data(argv[1], features)
    statistic_functions = [statistics.sum, statistics.mean, statistics.median]
    # seasons = [2,3]
    # s = set(seasons)
    # data.filter_by_feature(data, "season", s)
    #data.print_details(the_data, ["cnt"], statistic_functions)
    summer_data = data.filter_by_feature(the_data,"season",[1])
    print("Question 1:")
    print("Summer:")
    data.print_details(summer_data, ["hum","t1","cnt"], statistic_functions)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)