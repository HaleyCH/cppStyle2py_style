import sys

fp = sys.argv[1]
# fp = r"C:\Users\16173\CLionProjects\ACM_cpp\ListNode.cpp"
fn = fp.split(".")[0] + "_trans." + fp.split(".")[1]

content = ""
with open(fp, "r") as r_obj:
    with open(fn, "w") as w_obj:
        while True:
            line = ""
            s = r_obj.readline()
            if s == "":
                break
            for word in s.split(" "):
                if word == "":
                    line += " "
                    continue
                line += " " + word[0]
                if len(word) == 1:
                    continue
                for c in word[1:]:
                    if c.isupper():
                        line += "_"
                        c = c.lower()
                    line += c
            line = line.replace("\n", "")
            if len(line) < 72 and line[-1] in [":", "{", "}", ";"]:
                c = line[-1]
                line = line[0:-1]
                while len(line) < 71:
                    line += " "
                line += c + "\n"
            w_obj.write(line)
            print(line)
