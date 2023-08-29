from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_text = request.form.get('todo')
    todos.append({'text': todo_text, 'done': False})
    return redirect(url_for('index'))


@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    todos[todo_id]['done'] = True
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
