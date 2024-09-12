from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

# Home route to display tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:
        tasks.append({'task': task, 'completed': False})
    return redirect('/')

# Route to mark a task as completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks[task_id]['completed'] = True
    return redirect('/')

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
