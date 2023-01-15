Filename = 'todos.txt'


def get_todos(filename=Filename):
    """ To Read the textfile 'todos4.txt' line by line and return the list of todos  """

    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename=Filename):  # order is important, first non-default args then default

    """ to write the textfile 'todos4.txt' line by line and edit the todos4 in the list """

    with open(filename, 'w') as file_local:
        file_local.writelines(todos_arg)

