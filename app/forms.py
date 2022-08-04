from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class IntegerForm(FlaskForm):
    integer = IntegerField(
        'Ваше число для проверки',
        validators=[
            DataRequired(message='Обязательное поле'),
        ]
    )
    submit = SubmitField('Проверить')
