import sys
import data
from statistics import sum, mean, median, population_statistics


THRESHOLD = 13.0


def main(argv):
    """ Calculates and prints statistic values for features of records from the data
        collected in london.csv file.

        :parameter:
        argv -- list of arguments supplied (file to run, csv file address, features to get from the csv)
        :returns: None
    """
    # Question 1
    # Saves the features given in a list
    features = (argv[2].split(sep=", "))
    the_data = data.load_data(argv[1], features)
    statistic_functions = [sum, mean, median]
    # Saves the relevant records
    summer_data, not_summer = data.filter_by_feature(the_data, "season", [1])
    holiday_data, not_holiday = data.filter_by_feature(the_data, "is_holiday", [1])
    print("Question 1:")
    print("Summer:")
    data.print_details(summer_data, ["hum", "t1", "cnt"], statistic_functions)
    print("Holiday:")
    data.print_details(holiday_data, ["hum", "t1", "cnt"], statistic_functions)
    print("All:")
    data.print_details(the_data, ["hum", "t1", "cnt"], statistic_functions)

    # Question 2
    print("\nQuestion 2")
    print("If t1<=13.0, then:")
    # Saves the relevant records
    winter_data, not_winter = data.filter_by_feature(the_data, "season", [3])
    w_h_data, not_w_h_data = data.filter_by_feature(winter_data, "is_holiday", [1])
    population_statistics("Winter holiday records:", w_h_data, "t1", ["cnt"], THRESHOLD, 0, statistic_functions[1:])
    population_statistics("Winter weekday records:", not_w_h_data, "t1", ["cnt"], THRESHOLD, 0, statistic_functions[1:])
    print("If t1>13.0, then:")
    population_statistics("Winter holiday records:", w_h_data, "t1", ["cnt"], THRESHOLD, 1, statistic_functions[1:])
    population_statistics("Winter weekday records:", not_w_h_data, "t1", ["cnt"], THRESHOLD, 1, statistic_functions[1:])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)
