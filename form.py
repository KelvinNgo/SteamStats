from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired


class WordSearchForm(FlaskForm):

    steam_id = StringField('SteamID', validators=[InputRequired()],
                render_kw={"placeholder": "Input your steam ID"})
    submit = SubmitField('Go')
    dropdown_list = ['Low to High', 'High to Low']
    dropdown = SelectField('Sort Types', choices=dropdown_list, default=1)
