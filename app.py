from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from cafeform import CafeForm
import csv
from dotenv import load_dotenv
from os import getenv
app = Flask(__name__)
app.secret_key = getenv('SECRET_KEY')
Bootstrap5(app)


# Exercise:
# add: Location URL, open time, closing time, coffee rating, Wi-Fi rating, power outlet rating fields
# make coffee/Wi-Fi/power a select element with choice of 0 to 5.
# e.g., You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['get', 'post'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        append_to_csv(form.data)
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with if form.validate_on_submit()
    return render_template('add.html', form=form)


def append_to_csv(cafe_list):
    with open('cafe-data.csv', encoding='utf-8', newline='', mode='a') as db:
        csv_data = csv.writer(db, delimiter=',')
        # remove submit status and CSRF token
        cafe_list.popitem()
        cafe_list.popitem()
        csv_data.writerow(cafe_list.values())


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
