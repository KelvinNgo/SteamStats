
from flask import Flask, render_template, request
from form import WordSearchForm
from dotenv import load_dotenv
import os
from get_total_playtime import get_total_hours
from get_profile import get_profile_info

load_dotenv()


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
    return render_template("base.html", form=form)


if __name__ == "__main__":
    print(SECRET_KEY)
    app.run()