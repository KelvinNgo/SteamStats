from flask import Flask, render_template, request
from form import WordSearchForm
from dotenv import load_dotenv
import os
from get_total_playtime import get_total_hours
from get_profile import get_profile_info
from game_completion_profile import game_completion_profile

load_dotenv()

test = [{'gamename': 'Counter-Strike: Condition Zero', 'gamepic':
    'https://howlongtobeat.com/games/256px-CounterstrikeZerobox.jpg', 'percentcomplete': 0.0},
        {'gamename': 'Counter-Strike: Condition Zero Deleted Scenes', 'gamepic':
            'https://howlongtobeat.com/games/256px-ConditionZerobox.jpg', 'percentcomplete': 0.0}]

SECRET_KEY = os.getenv("SECRET_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz'  # this isn't that important
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET", "POST"])
def search():
    form = WordSearchForm()
    if form.validate_on_submit() and request.form['steam_id'].strip():
        query = request.form['steam_id']
        profile_data = get_profile_info(SECRET_KEY, query)[0]
        return render_template("loading.html", data=query.strip(), form=form, profile=profile_data)
        display_stats()
        # return render_template("stats_display.html", stats=test)
    return render_template("base.html", form=form)


@app.route("/loading")
def loading(data, form, profile):
    return render_template("loading.html", data=data, form=form, profile=profile)


def display_stats():
    query = request.form['steam_id']
    # stats = game_completion_profile(get_total_hours(SECRET_KEY, query))
    return render_template("stats_display.html", stats=test)


if __name__ == "__main__":
    app.run()
