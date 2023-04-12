from flask import render_template, redirect, url_for, flash
from self_dev import app, db
from self_dev.forms import GoalForm, HabitForm, JournalForm
from self_dev.models import Goal, Habit, Journal

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/goals', methods=['GET', 'POST'])
def goals():
    form = GoalForm()
    if form.validate_on_submit():
        goal = Goal(title=form.title.data, description=form.description.data)
        db.session.add(goal)
        db.session.commit()
        flash('Your goal has been saved.')
        return redirect(url_for('goals'))
    goals = Goal.query.all()
    return render_template('goals.html', goals=goals, form=form)

@app.route('/habits', methods=['GET', 'POST'])
def habits():
    form = HabitForm()
    if form.validate_on_submit():
        habit = Habit(title=form.title.data, description=form.description.data)
        db.session.add(habit)
        db.session.commit()
        flash('Your habit has been saved.')
        return redirect(url_for('habits'))
    habits = Habit.query.all()
    return render_template('habits.html', habits=habits, form=form)

@app.route('/habits/<int:habit_id>/delete', methods=['POST'])
def delete_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    db.session.delete(habit)
    db.session.commit()
    flash('Your habit has been deleted.')
    return redirect(url_for('habits'))


@app.route('/journal', methods=['GET', 'POST'])
def journal():
    form = JournalForm()
    if form.validate_on_submit():
        journal = Journal(title=form.title.data, content=form.content.data)
        db.session.add(journal)
        db.session.commit()
        flash('Your journal entry has been saved.')
        return redirect(url_for('journal'))
    entries = Journal.query.all() # change variable name to entries
    return render_template('journal.html', entries=entries, form=form)

@app.route('/goals/<int:goal_id>/delete', methods=['POST'])
def delete_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    db.session.delete(goal)
    db.session.commit()
    flash('The goal has been deleted!', 'success')
    return redirect(url_for('goals'))

@app.route('/journal/delete/<int:id>', methods=['POST'])
def delete_journal_entry(id):
    entry = Journal.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    flash('Your journal entry has been deleted.')
    return redirect(url_for('journal'))







