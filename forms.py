
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, TextAreaField
from wtforms.validators import InputRequired
from useful_functions import ideas_radio


class InitialIdeasForm(FlaskForm):
    idea = TextAreaField \
        ('A clear area requiring improvement in order for Freudenberg risk management and compliance to be better understood is ', validators=[InputRequired()], render_kw={"rows": 1, "cols": 25})
    submit = SubmitField('(no more than 5 words). Submit here.')


class DevelopedIdeasForm(FlaskForm):
    idea = TextAreaField \
        ('A way of solving one of the improvement ideas above could be ', validators=[InputRequired()], render_kw={"rows": 1, "cols": 25})
    submit = SubmitField('(no more than 5 words). Submit here.')


class VotingForm(FlaskForm):
    vote = TextAreaField \
        ('copy your favourite idea here: ', validators=[InputRequired()], render_kw={"rows": 1, "cols": 45})
    submit = SubmitField('Submit')


class AdminForm(FlaskForm):
    vote = RadioField('vote:', choices=[("generate initial 80","generate initial 80"),("generate developed 80","generate developed 80"),("generate initial 10 ideas","generate initial 10 ideas"),("calculate top 4 votes","calculate top 4 votes"),("generate developed 5 ideas","generate developed 5 ideas")], validators=[InputRequired()])
    submit = SubmitField('Submit')
