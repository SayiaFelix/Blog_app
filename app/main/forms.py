from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add Your Bio ::',validators = [DataRequired()])
    submit = SubmitField('Upload')

class BlogForm(FlaskForm):
    title = StringField('Post Title ::')
    topic = StringField('Topic ::')
    content = TextAreaField('Post Content ::')
    submit = SubmitField('Post Blog ')

class CommentForm(FlaskForm):

    comment = TextAreaField('Drop Comment ::')
    submit = SubmitField('Submit Comment')

class SubscriberForm(FlaskForm):

    email = StringField('Email Address ::')
    name = StringField('Enter your name ::',validators = [DataRequired()])
    submit = SubmitField('Subscribe')