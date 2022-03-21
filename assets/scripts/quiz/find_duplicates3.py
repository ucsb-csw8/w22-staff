# Expects the infile to come from Gradescope
# with the additional last column "Version"
# The scores for all versions are all together:
# this file is identifying the students who opened
# more than one version.
# The resulting file has the max score across different
# versions stored for the students with duplicate scores.
import csv

def remove_duplicate_records(infile):
    #infile = 'Quiz_2_scores.csv'
    outfile = infile.replace('.', "-no-duplicates.")
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
            if len(sid) < 7:
                print("Not a valid student SID")
                print(row)
                continue
            score = float(row[5])
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
                    continue
                else:
                # Add the new version:score to the dictionary
                    print("{} : upgrading score from {} --> {}".format(sid, stored_score, score))
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
