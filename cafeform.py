from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = URLField(label='Google Map location', validators=[DataRequired()])
    opening_time = TimeField(label='Opening hours e.g 08:00 AM', validators=[DataRequired()])
    closing_hour = TimeField(label='Closing hours e.g 08:00 PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=['☕☕☕☕', '☕☕☕', '☕☕', '☕'], validators=[DataRequired()])
    wifi_strength = SelectField(label='WI-FI Strength Rating', choices=['💪💪💪💪', '💪💪💪', '💪💪', '💪'], validators=[DataRequired()])
    power_socket_availability = SelectField(label='Power Socket Availability', choices=['💪💪💪💪', '💪💪💪', '💪💪', '💪'], validators=[DataRequired()])
    submit = SubmitField('Submit')
