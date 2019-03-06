input_file = open("a_example.txt", "r")
output_file = open("submissionA.txt", "w")

slides = float(0)
cline = int(0)
citems = int(0)
tag_dict = {}

for line_str in input_file:
    cline += 1
    ls2 = line_str.split()
    for x in ls2:
        print("enter/pass")
        citems += 1
        if cline == 1:
            print("if 1")
            citems = 0
            break
        elif citems == 1:
            print("if 2")
            # Count slides
            if x == "H":
                slides += 1
                pass
            elif x == "V":
                slides += 0.5
                pass
            # if elif for H or V
        elif citems == 2:
            print("if 3")
            pass
        # increment citem if second param
        print("if 4")
        if x in tag_dict:
            val = cline = cline - 1
            tag_dict[x] = tag_dict[x].append(val)
        else:
            tag_dict[x] = []
        # add tag if not in dict else append photo number

print(tag_dict.keys())
tag_dict.clear()
input_file.close()
output_file.close()