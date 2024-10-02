import os.path

def read_files(directory) -> dict:
    fds = sorted(os.listdir(directory))
    lens_files = {}
    for file in fds :
        with open(directory + file, "r") as f:
            data_file = f.read().splitlines()
        lens_files[len(data_file)] = f
    return lens_files

def file_handler(lens_files) -> str:
    result_text = ""
    for length, file in sorted(lens_files.items()):
        file = open(file.name)
        filename = os.path.basename(file.name)
        data = file.read().splitlines()
        result_text += filename + "\n" + str(length) + "\n" + "\n".join(data) + "\n"
        file.close()
    return  result_text

if __name__ == '__main__':
    dir = "files/"
    len_file = read_files(dir)
    text = file_handler(len_file) # можно функцию сделать void и она внутри будет записывать в файл
    # но с расширением кода читаемость будет ухудшаться
    with open("files/result.txt", "a") as result_file:
        result_file.write(text)