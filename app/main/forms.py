from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add Your Bio ::',validators = [DataRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Blog Title ::')
    topic = StringField('Topic ::')
    content = TextAreaField('Blog Content ::')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Drop Comments')

class SubscriberForm(FlaskForm):

    email = StringField('Email Address ::')
    name = StringField('Enter your name ::',validators = [DataRequired()])
    submit = SubmitField('Subscribe')