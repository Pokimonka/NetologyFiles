import os.path

with open("files/1.txt", "r") as file1:
    data_file1 = file1.read().splitlines()

with open("files/2.txt", "r") as file2:
    data_file2 = file2.read().splitlines()

with open("files/3.txt", "r") as file3:
    data_file3 = file3.read().splitlines()

lens_files = {len(data_file1): file1, len(data_file2): file2, len(data_file3): file3}
for length, file in sorted(lens_files.items()):
    file = open(file.name)
    filename = os.path.basename(file.name)
    data = file.read().splitlines()
    with open("files/result.txt", "a") as result_file:
        result_file.write(filename + "\n")
        result_file.write(str(length) + "\n")
        result_file.write("\n".join(data) + "\n")
    file.close()

