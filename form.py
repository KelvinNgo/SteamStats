from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class WordSearchForm(FlaskForm):

    steam_id = StringField('SteamID', validators=[InputRequired()],
                render_kw={"placeholder": "Input your steam ID:"})
    submit = SubmitField('Go')
