from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    avg_rating = StringField('Rating', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    pub_id = StringField('Publisher', validators=[DataRequired()])
    submit = SubmitField('Submit')