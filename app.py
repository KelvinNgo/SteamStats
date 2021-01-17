from flask import Flask, render_template, request
from form import WordSearchForm
from dotenv import load_dotenv
import os
from get_total_playtime import get_total_hours
from get_profile import get_profile_info
from game_completion_profile import game_completion_profile

load_dotenv()

test = [{'gamename': 'Fallout: New Vegas', 'gamepic': 'https://howlongtobeat.com/games/Fallout_New_Vegas.jpg', 'percentcomplete': 31.52, 'hourslogged': '8.67'}, {'gamename': 'Magicka', 'gamepic': 'https://howlongtobeat.com/games/Magicka_box.jpg', 'percentcomplete': 5.71, 'hourslogged': '0.60'}, {'gamename': 'Terraria', 'gamepic': 'https://howlongtobeat.com/games/Terraria_292x136.jpg', 'percentcomplete': 71.04, 'hourslogged': '65.00'}]

SECRET_KEY = os.getenv("SECRET_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz'  # this isn't that important
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET", "POST"])
def search():
    form = WordSearchForm()
    if form.validate_on_submit() and request.form['steam_id'].strip():
        query = request.form['steam_id']
        stats = game_completion_profile(get_total_hours(SECRET_KEY, query))
        profile = get_profile_info(SECRET_KEY, query)[0]
        return render_template("stats_display.html", stats=stats, profile=profile)
    return render_template("base.html", form=form)


@app.route("/loading")
def loading(data, form, profile):
    return render_template("loading.html", data=data, form=form, profile=profile)


@app.route("/stats_display")
def display_stats():
    query = request.form['steam_id']
    stats = game_completion_profile(get_total_hours(SECRET_KEY, query))
    return render_template("stats_display.html", stats=stats)


if __name__ == "__main__":
    app.run()
