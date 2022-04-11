def MemberPay(numberOfWeek):
    file = "MemberFile"
    if numberOfWeek > 4 or numberOfWeek == 0:
        return Exception
    num_lines = sum(1 for line in open(file))
    reading_file = open(file, "r")
    n = 0
    new_file_content = ""
    for line in reading_file:
        n += 1
        new_line = line.strip()
        if n == 3:
            new_line = line.strip()
            for i in range(numberOfWeek):
                if new_line[-2] == " ":
                    base = int(new_line[-1])
                else:
                    base = int(new_line[-2] + new_line[-1])
                new_line = new_line + " " + str(base + 1)

        new_file_content += new_line + "\n"
    if num_lines == 2:
        new_line = "1"
        for i in range(1, numberOfWeek):
            to_add = int(new_line[-1])
            new_line = new_line + " " + str(to_add + 1)
        new_file_content += new_line + "\n"
    reading_file.close()

    writing_file = open("MemberFile", "w")
    writing_file.write(new_file_content)
    writing_file.close()
    return