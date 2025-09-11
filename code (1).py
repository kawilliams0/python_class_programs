from flask import Flask, render_template_string, request, redirect
import json
import datetime

app = Flask(__name__)
TASKS_FILE = "tasks.json"

# Helper functions to load/save tasks from the JSON file
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# The HTML template for our web page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✨ TidyTasks ✨</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f0f2f5; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        h1 { text-align: center; color: #333; }
        .task-list { list-style: none; padding: 0; }
        .task-item { display: flex; align-items: center; padding: 10px; border-bottom: 1px solid #eee; }
        .task-item.completed span { text-decoration: line-through; color: #aaa; }
        .task-item span { flex-grow: 1; }
        .task-actions a { text-decoration: none; padding: 5px 10px; border-radius: 5px; margin-left: 5px; color: white; }
        .complete-btn { background-color: #28a745; }
        .delete-btn { background-color: #dc3545; }
        form { display: flex; margin-top: 20px; }
        input[type="text"] { flex-grow: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px 0 0 5px; }
        button { padding: 10px 15px; border: none; background-color: #007bff; color: white; border-radius: 0 5px 5px 0; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>✨ TidyTasks ✨</h1>
        <ul class="task-list">
            {% for task in tasks %}
            <li class="task-item {% if task.status == 'completed' %}completed{% endif %}">
                <span>{{ '✅' if task.status == 'completed' else '⏳' }} {{ task.description }}</span>
                <div class="task-actions">
                    {% if task.status == 'pending' %}
                    <a href="/complete/{{ loop.index0 }}" class="complete-btn">✔️</a>
                    {% endif %}
                    <a href="/delete/{{ loop.index0 }}" class="delete-btn">🗑️</a>
                </div>
            </li>
            {% endfor %}
        </ul>
        <form action="/add" method="post">
            <input type="text" name="description" placeholder="📝 Add a new task..." required>
            <button type="submit">Add</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    tasks = load_tasks()
    description = request.form.get('description')
    if description:
        new_task = {
            "description": description,
            "status": "pending",
            "created_at": datetime.date.today().isoformat()
        }
        tasks.append(new_task)
        save_tasks(tasks)
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['status'] = 'completed'
        save_tasks(tasks)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    # The host='0.0.0.0' makes it accessible from your phone on the same network
    app.run(host='0.0.0.0', port=5000, debug=True)