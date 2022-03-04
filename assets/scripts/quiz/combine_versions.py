# Expects the infile to come from Gradescope.
# Adds a new last column "Version"
# Assembles the scores for all versions into one file,
# ignoring the rows for students that contain "Missing"
# Since those are usually at the end of the file,
# the processing of those stops when the first "Missing"
# is encountered.
# Call using combine_scores("Quiz 9", 5)
import csv

#version = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
version = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

def check_existence(file_prefix, num_versions):
    """ Looks for the existence of the CSV files
        named <file_prefix>_<version>__scores.csv"""
    for n in range(num_versions):
        fname = "{}_{}__scores.csv".format(file_prefix, version[n])
        print("Reading", fname)
        file = open(fname, 'r')
        file.close()
        
def remove_missing(file_prefix, num_versions):
    """ Looks for the CSV files named
        <file_prefix>_<version>__scores.csv
        Writes a new file (adds "no-missing" before .csv
        in the new filename) with the missing records removed.
    """
    total = 0
    for n in range(num_versions):
        fname = "{}_{}__scores.csv".format(file_prefix, version[n])
        outfile = fname.replace('.', "-no-missing.")
        print("Reading", fname)
        file = open(fname, 'r')
        print("Writing", outfile)
        writer = open(outfile, 'w')
        file_total = -1 # since there's a header row
        for row in file:
            if "Missing" not in row:
                data = row.split(",")
                # Check that it's a valid student record
                if len(data[0]) > 1 and len(data[1]) > 1:
                    writer.write(row)
                    file_total += 1
                else:
                    print("Omitting an invalid student record")
                    print(data)
            else:
                total += file_total
                print("Wrote", file_total, "records")
                #print("Got to the missing records. Moving on.")
                #print(row)
                break
        file.close()
        writer.close()
    print("Processed", total, "student records.")

def assemble_scores(file_prefix, num_versions):
    """ Looks for the CSV files named
        <file_prefix>_<version>__scores-no-missing.csv.
        Writes each row from that file and adds a new column
        "Version" to the end of each row in a new file
        called"<file_prefix>_scores.csv".
    """
    outfile = file_prefix + "_scores.csv"
    print("Writing", outfile)
    file_writer = open(outfile, "w") #csv.writer(outfile, "w")
    writer = csv.writer(file_writer)
    total = 0
    first_file = True # use it to write the header only once
    for n in range(num_versions):
        fname = "{}_{}__scores-no-missing.csv".format(file_prefix, version[n])     
        print("Reading", fname)
        file = open(fname, 'r')
        first_row = True
        #all_rows = file.readlines()
        grades_reader = csv.reader(fname, delimiter=',')
        for row in grades_reader:
            #print(row)
            #row = row.split(',')
            if first_row and first_file:
                row.append("Version")
                writer.writerow(row)
                first_row = False
                first_file = False
                continue
            elif first_row == True:
                first_row = False # skip the header row
                continue
            row.append(version[n])
            print(row)
            writer.writerow(row)
            break
        file.close()
    #writer.close()
    file_writer.close()
    print("Processed", total, "student records.")


def combine_scores(file_prefix, num_versions):
    """ Looks for the CSV files named
        <file_prefix>_<version>__scores-no-missing.csv.
        Writes each row from that file and adds a new column
        "Version" to the end of each row in a new file
        called"<file_prefix>_scores.csv".
    """
    outfile = file_prefix + "_scores.csv"
    print("Writing", outfile)
    file_writer = open(outfile, "w")
    write_csv = csv.writer(file_writer)
    
    total = 0
    first_file = True # use it to write the header only once
    for n in range(num_versions):
        fname = "{}_{}__scores-no-missing.csv".format(file_prefix, version[n])     
        print("Reading", fname)
        file_reader = open(fname, 'r')
        first_row = True
        grades_reader = csv.reader(file_reader)
        file_total = 0
        for row in grades_reader:
            #print(row)
            #row = row.split(',')
            if first_row and first_file:
                row.append("Version")
                write_csv.writerow(row)
                first_row = False
                first_file = False
                continue
            elif first_row == True:
                first_row = False # skip the header row
                continue
            row.append(version[n])
            #print(row)
            write_csv.writerow(row)
            file_total += 1
            #break
        file_reader.close()
        print("Wrote", file_total, "records from version", version[n])
        total+= file_total
    #writer.close()
    file_writer.close()
    print("Processed", total, "student records.")
   
"""
outfile = 'Quiz_3_scores.csv'

print("Reading", infile)
first_line = True
with open(infile, 'r') as myfile:
    data = {}
    name = {}
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        if first_line == True:
            first_line = False
            continue
        # Use the first 5 values and the last (version).
        # First Name, Last Name, SID, Email, Total Score
        # Max Points, Status, Submission ID, Submission Time, Lateness (H:M:S)	View Count	1: Quiz Version (1.0 pts)	2: Short answer (3.0 pts)	3 (5.0 pts)
        # Version
        sid = row[2]
        score = float(row[4])
        cur_version = row[-1]
        fname = row[0]
        lname = row[1]
        if name.get(sid) == None: # if a new student
            name[sid] = (sid, fname, lname)
        if data.get(sid) == None: # if a new student
            # Store Version, Max score, {Version:Score}
            # data[sid][0] ==> Version
            # data[sid][1] ==> Max score
            # data[sid][2] ==> Dictionary with all version:score mapping
            data[sid] = (cur_version, score, {cur_version: score})
        else: # Already have a score for this student
            print(fname, lname, sid, score, cur_version)
            print(data[sid]) # what we already have
            stored_score = data[sid][1]
            if stored_score > score:
                print("{}: A higher score {} --> {}".format(sid, stored_score, score))
            else:
                # Add the new version:score to the dictionary
                data[sid][2][cur_version] = score
                # Update the record to the new high score
                data[sid] = (cur_version, score, data[sid][2])
                print(data[sid])

print("Writing", outfile)
with open(outfile, 'w') as csvfile:
    grades_writer = csv.writer(csvfile)

    row = ["SID", "First name", "Last name", "Quiz version", "Score", "Notes"]
    grades_writer.writerow(row)
    total = 0
    for sid in name:
        row = list(name[sid]) + [data[sid][0], data[sid][1], str(data[sid][2])]
        grades_writer.writerow(row)
        total += 1
print("Finished writing", total, "records.")
"""
