from flask import Flask, render_template, request
from form import WordSearchForm
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/Hack-the-North-2021')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env.key'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET", "POST"])
def search():
    form = WordSearchForm()
    if form.validate_on_submit() and request.form['steam_id'].strip():
        query = request.form['steam_id']
        return render_template("base.html", data=query.strip(), form=form)
    return render_template("base.html", form=form)


if __name__ == "__main__":
    app.run()
