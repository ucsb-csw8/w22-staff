import csv
gauchospace = "gauchospace.csv"
gradescope = "gradescope.csv"
perm_index = 2
dt_len = len('2022-03-15 08:12:38')
time_limit = 45


def get_minutes(some_time):
    hours, minutes = some_time.split(':')
    return int(hours) * 60 + int(minutes)


def get_dict_from_csv(filename):
    file_dict = dict()
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        fields = next(csv_reader)
        print(fields)
        for row in csv_reader:
            file_dict[row[perm_index]] = row
    return file_dict


def print_late_submissions():
    gauchospace_dict = get_dict_from_csv(gauchospace)
    gradescope_dict = get_dict_from_csv(gradescope)

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