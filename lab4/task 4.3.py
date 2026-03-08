def file_manage(txt: str, filename: str):
    with open(filename, "a",encoding="UTF-8") as f:
        f.write(f"\n{txt}")

    with open(filename, "r",encoding="UTF-8") as f:
        res = f.readlines()
        for index, line in enumerate(res):
            if index % 2 == 0:
                print(f"{line}")

# txt = ("line1\n"
#        "line2\n"
#        "line3\n"
#        "line4\n"
#        "line5\n")

file_manage("line4","test.txt")
