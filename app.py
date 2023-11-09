from flask import Flask, render_template, request

import useful_functions
from forms import InitialIdeasForm, VotingForm, DevelopedIdeasForm, AdminForm

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='')
app.config['SECRET_KEY'] = 'd4nny'


@app.route('/', methods=['GET', 'POST'])
def home():
    title = 'Home'
    form = InitialIdeasForm()
    if request.method == 'POST':
        useful_functions.add_idea(form.idea.data, "Initial_Ideas")
    return render_template('home.html', title=title, form=form)


@app.route('/initial_10', methods=['GET', 'POST'])
def initial_10():
    title = 'vote'
    ideas= useful_functions.ideas_radio("Initial_10_Ideas")
    form = VotingForm()
    if request.method == 'POST':
        useful_functions.update_vote(form.vote.data)
    return render_template('initial_10.html', title=title, form=form,ideas=ideas)


@app.route('/add_developed', methods=['GET', 'POST'])
def add_developed():
    title = 'developed'
    form = DevelopedIdeasForm()
    ideas = useful_functions.fetch_ideas("Top_4_Ideas")
    if request.method == 'POST':
        useful_functions.add_idea(form.idea.data, "Developed_Ideas")
    return render_template('add_developed.html', title=title, form=form, ideas=ideas)


@app.route('/developed_5', methods=['GET', 'POST'])
def developed_5():
    title = 'developed_5'
    ideas = useful_functions.fetch_ideas("Developed_5_Ideas")
    return render_template('developed_5.html', title=title, ideas=ideas)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    title = 'admin'
    form = AdminForm()
    if request.method == 'POST':
        if form.vote.data == "generate initial 80":
            useful_functions.generate_ideas("Initial_Ideas")
        elif form.vote.data == "generate developed 80":
            useful_functions.generate_ideas("Developed_Ideas")
        elif form.vote.data == "generate initial 10 ideas":
            useful_functions.generate_initial_10()
        elif form.vote.data == "calculate top 4 votes":
            useful_functions.voting_calculator()
        elif form.vote.data == "generate developed 5 ideas":
            useful_functions.generate_developed_5()


    return render_template('admin.html', title=title, form=form)


if __name__ == "__main__":
    app.run(debug=True)
