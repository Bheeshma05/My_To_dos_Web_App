import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():

    todo_local = st.session_state['new_todo'] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title("My To-do App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)

        del st.session_state[todo]
        st.experimental_rerun()

todo = st.text_input(label='Enter a todo:',
                     placeholder='Enter a todo',
                     on_change=add_todo,
                     key='new_todo')
