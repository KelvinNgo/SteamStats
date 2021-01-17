from flask import Flask, render_template, request
from form import WordSearchForm
from dotenv import load_dotenv
import os
from get_total_playtime import get_total_hours
from sorting_algorithms import merge_sort_low_high, merge_sort_high_low
from game_completion_profile import game_completion_profile

load_dotenv()

test = [{'gamename': 'Counter-Strike: Condition Zero', 'gamepic':
    'https://howlongtobeat.com/games/256px-CounterstrikeZerobox.jpg', 'percentcomplete': 0.0},
        {'gamename': 'Counter-Strike: Condition Zero Deleted Scenes', 'gamepic':
            'https://howlongtobeat.com/games/256px-ConditionZerobox.jpg', 'percentcomplete': 0.0},
        {'gamename': "Garry's Mod", 'gamepic': 'https://howlongtobeat.com/games/GarrysMod_292x136.jpg',
         'percentcomplete': 6.31}, {'gamename': 'Killing Floor', 'gamepic':
        'https://howlongtobeat.com/games/4983_Killing_Floor.jpg', 'percentcomplete': 14.59},
        {'gamename': 'Fallout: New Vegas', 'gamepic': 'https://howlongtobeat.com/games/Fallout_New_Vegas.jpg',
         'percentcomplete': 31.52}, {'gamename': 'Magicka', 'gamepic':
        'https://howlongtobeat.com/games/Magicka_box.jpg', 'percentcomplete': 5.71},
        {'gamename': 'Terraria', 'gamepic': 'https://howlongtobeat.com/games/Terraria_292x136.jpg',
         'percentcomplete': 71.04}]

SECRET_KEY = os.getenv("SECRET_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz'  # this isn't that important
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET", "POST"])
def search():
    form = WordSearchForm()
    if form.validate_on_submit() and request.form['dropdown'] == "Low to High":
        query = request.form['steam_id']
        stats = merge_sort_low_high(game_completion_profile(get_total_hours(SECRET_KEY, query)))
        return render_template("stats_display.html", stats=stats)

    elif form.validate_on_submit() and request.form['dropdown'] == "High to Low":
        query = request.form['steam_id']
        stats = merge_sort_high_low(game_completion_profile(get_total_hours(SECRET_KEY, query)))
        return render_template("stats_display.html", stats=stats)

    return render_template("base.html", form=form)


@app.route("/loading")
def loading(data, form, profile):
    return render_template("loading.html", data=data, form=form, profile=profile)


@app.route("/stats_display")
def display_stats():
    query = request.form['steam_id']
    stats = game_completion_profile(get_total_hours(SECRET_KEY, query))
    return render_template("stats_display.html", stats=test)


if __name__ == "__main__":
    app.run()
