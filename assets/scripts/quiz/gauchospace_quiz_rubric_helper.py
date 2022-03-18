# add all the viable options to the below list
responses = ["for (idx, city) in enumerate(capital):"]
seps = [" ", "(", ")", ",", ":"]
for response in responses:
    output = response
    for sep in seps:
        output = f"<SPACE>{sep}<SPACE>".join(output.split(sep))
    print(("<SPACE>" + output).replace("<SPACE> <SPACE>", "<SPACE>").replace("<SPACE><SPACE>", "<SPACE>"))