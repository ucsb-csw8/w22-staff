print("Processing quiz scores")
print("Run get_quiz_scores(prefix, n_versions)")
print("The script will use n_versions to add A, B, etc.)")
print("to look for files <file_prefix>_[letter]__scores.csv")
print("to create <file_prefix>_scores.csv")
# Call using get_quiz_scores("Quiz_9", 5)
# The file to use for gauchospace upload
# is named <file_prefix>_scores.csv,
# e.g. Quiz_9_scores.csv

from find_duplicates3 import *
from combine_versions import *

def get_quiz_scores(prefix, n_versions, suffix):
    # Check that the required files exist/named correctly
    check_existence(prefix, n_versions, suffix)
    
    # Create intermediate files that have no missing records
    # <file_prefix>_<version>__scores-no-missing.csv
    remove_missing(prefix, n_versions, suffix)
    
    # Read all <file_prefix>_<version>__scores-no-missing.csv
    # Create a unified file that holds all records
    # <file_prefix>_scores.csv
    
    combine_scores(prefix, n_versions, suffix)
    # Open <file_prefix>_scores.csv
    # Remove duplicate records and store the result in
    # <file_prefix>_scores-no-duplicates.csv
    filename = prefix + "_scores.csv"
    remove_duplicate_records(filename)


get_quiz_scores("_Version", 5, "Week_5_Pop-Quiz_2")