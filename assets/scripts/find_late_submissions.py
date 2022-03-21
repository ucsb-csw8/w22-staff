import csv
gauchospace = "gauchospace.csv"
gradescope = "gradescope.csv"
gauchospace_perm_index = 2
gradescope_perm_index = 2
dt_len = len('2022-03-15 08:12:38')
time_limit = 45


def get_minutes(some_time):
    """
    convert some_time ( format -> hh:mm ) to minutes
    """
    hours, minutes = some_time.split(':')
    return int(hours) * 60 + int(minutes)


def get_dict_from_csv(filename, perm_index):
    """
    filename : should be a csv file, either from gradescope or gauchospace, where the column at perm_index
    should contain the perm number of the student, so that it can be used as key for the dict being created.
    returns file_dict
    key : perm_number
    value : the corresponding csv row
    """
    file_dict = dict()
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        fields = next(csv_reader)
        print(fields)
        for row in csv_reader:
            file_dict[row[perm_index]] = row
    return file_dict


def print_late_submissions():
    """
    loads two csv files, one from gauchospace and the other one from gradescope.
    Creates a dict for each of the files, using perm_number as key.
    Picks the start_time from gauchospace, end_time from gradescope.
    checks if the total quiz duration is more than the time_limit, and displays the
    first_name, last_name, perm_number of the student.
    start_time -> column index 5 in the gauchospace file
    end_time -> column index 9 in the gradescope file
    """
    gauchospace_dict = get_dict_from_csv(gauchospace, gauchospace_perm_index)
    gradescope_dict = get_dict_from_csv(gradescope, gradescope_perm_index)

    late_submissions = []
    for grade_key, grade_row in gradescope_dict.items():
        if grade_key in gauchospace_dict:
            gaucho_row = gauchospace_dict[grade_key]
            gaucho_start_time = gaucho_row[5].split()[3]
            gaucho_start_time = get_minutes(gaucho_start_time)
            grade_end_time = grade_row[9][0:dt_len].split()[1][:5]
            grade_end_time = get_minutes(grade_end_time)
            # print(gaucho_start_time, grade_end_time, grade_end_time-gaucho_start_time, sep=' , ')
            if grade_end_time-gaucho_start_time > time_limit:
                late_submissions.append(grade_row[:3] + [str(grade_end_time - gaucho_start_time) + ' mins'])

    print("Late submission!")
    print(*late_submissions, sep='\n')
