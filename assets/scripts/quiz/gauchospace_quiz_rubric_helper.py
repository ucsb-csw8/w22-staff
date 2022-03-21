"""
use this tiny script to generate the rubric options with unexpected spaces

sample_input :
c = x + y

sample_output :
<SPACE>c<SPACE>=<SPACE>x<SPACE>+<SPACE>y
"""
# add all the viable options to the below list
responses = ["for (idx, city) in enumerate(capital):", "c = x + y"]
seps = [" ", "(", ")", ",", ":"]
for response in responses:
    output = response
    for sep in seps:
        output = f"<SPACE>{sep}<SPACE>".join(output.split(sep))
    print(("<SPACE>" + output).replace("<SPACE> <SPACE>", "<SPACE>").replace("<SPACE><SPACE>", "<SPACE>"))