from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# SQLite データベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# タスクモデルの定義
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    deadline = db.Column(db.String(10), nullable=False)  # 例: 'YYYY-MM-DD'
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.task}>'

# 初回起動時にデータベースを作成
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks_todo = Task.query.filter_by(completed=False).all()
    tasks_done = Task.query.filter_by(completed=True).all()
    return render_template('index.html', tasks=tasks_todo, completed_tasks=tasks_done)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    deadline = request.form.get('deadline')
    if task_content and deadline:
        new_task = Task(task=task_content, deadline=deadline)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/restore/<int:task_id>')
def restore_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = False
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_completed/<int:task_id>')
def delete_completed_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/calendar')
def calendar():
    tasks = Task.query.all()
    events = [{'title': task.task, 'start': task.deadline} for task in tasks]
    return render_template('calendar.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
