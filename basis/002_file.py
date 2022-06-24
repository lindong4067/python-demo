import os

file_list = []

def find_hello(parent_dir, file_name):
    file_abspath = os.path.join(parent_dir, file_name)
    if os.path.isdir(file_abspath):
        for f in os.listdir(file_abspath):
            find_hello(file_abspath, f)
    else:
        if file_abspath.endswith('.py'):
            if read_and_find_hello(file_abspath):
                file_list.append(file_abspath)

def read_and_find_hello(py_file):
    flag = False
    f = open(py_file)
    while True:
        line = f.readline()
        if line == '':
            break
        elif 'hello' in line:
            flag = True
            break
    f.close()
    return flag

find_hello('C:\\PythonCode', 'python-demo')

print(file_list)
