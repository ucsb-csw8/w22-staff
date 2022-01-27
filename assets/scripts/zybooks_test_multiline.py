# (https://zybooks.zendesk.com/hc/en-us/articles/360018781373)
# after downloading the zyBooks test
# (use the XXX_with_answers document where
# correct answers marked with an asterisk (*)).
# Copy the questions and paste them into a plaintext doc.
# Manually remove the heading, so that the first Q is on the first line.
# then run this script to
# - remove the question numbers
# - detect the correct answer and add it to the Gauchospace version
# - convert the zyBook options to Gauchospace options
# For the final version, make sure to go over the output
# and correct the multi-line question to be on a single line
# we recommend adding _A at the start of that question,
# so that Gauchospace filters them all to the top, making it easier
# to edit (and to remove that _A tag when re-formatting the question).

def convert_zybooks_test(filepath):
    """
    Given a filepath, for a zyBooks file saved as a txt,
    where correct answers marked with an asterisk (*)),
    process it to

    Creates an output file with _gsp appended before `.txt`.
    The script expects 4 answer options, after which it adds
    the answer, which was marked with a *.
    The resulting file will have multi-line question all on the
    same line.
    """
    zoptions = ["a. ", "b. ", "c. ", "d. "] # zyBook format
    goptions = ["A. ", "B. ", "C. ", "D. "] # Gauchospace format
    answer_format = "ANSWER: " #e.g. ANSWER: A
    answer= ""
    
    print("Opening", filepath)
    testfile = open(filepath)
    result_filename = filepath.replace(".txt", "_gsp.txt")
    resultfile = open(result_filename, 'w')
    print("Saving", result_filename)
    
    start = -1
    for line in testfile:
        print(line) # DEBUGGING
        option_line = False # to help detect multi-line questions
        if line.isspace():
            resultfile.write(line) # write a single empty line
            continue
        # we are at the first line of a question
        start = line.find(")") + 1 # exclude )
        # we aren't creating 100 questions so start index should be 2 or 3
        if start != 0 and start < 4: 
            output = line[start:].strip(" ")
            #print("New line:", output)
            resultfile.write(output) # write a question w/o NN)
            continue 
        else:
            # find didn't find ) and find() returned -1
            start = -1
        # Check if we found one of the options
        for idx in range(len(zoptions)):
            if zoptions[idx] in line:
                if idx == 0:
                    # print("We are at the first option")
                    # If we are at the option A
                    # that follows a multi-line question,
                    # we might need a line break,
                    # since the previous line didn't have it
                    if output[-1] != '\n':
                        output = '\n'
                        resultfile.write(output)
                option_line = True # to help detect multi-line questions
                output = line.replace(zoptions[idx], goptions[idx])
                #print("New option:", output)
                if line[0] == "*": # correct option
                    answer = goptions[idx][0] # no punctuation
                    output = output.strip("*")
                resultfile.write(output)
                if idx == 3: # If we are at the last option, D
                    output = answer_format + answer + "\n"
                    resultfile.write(output)
                break
            """
            else:
                print("Line is", line)
                print("Didn't find", zoptions[idx])
            """
        # If we are here, we have a multi-line question, so
        # strip the whitespace and write it into the file
        if option_line == False:
            output = line.strip()
            resultfile.write(output)
        
    testfile.close()
    resultfile.close()
