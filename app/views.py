from flask import render_template

from . import app
from .forms import IntegerForm
from .models import SimpleResponse, ResultMessageText, ResultDividedStringCodes


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = IntegerForm()
    if not form.validate_on_submit():
        return render_template('index_denominator.html', form=form)
    integer = form.integer.data
    div_by_3 = integer % 3 == 0
    div_by_5 = integer % 5 == 0
    response = SimpleResponse(
        message=ResultMessageText.NO_DIV.value,
        string_code=ResultDividedStringCodes.NO_DIV.value
    )
    if div_by_3 and div_by_5:
        response.message = ResultMessageText.DIV_BY_THREE_AND_FIVE.value
        response.string_code = ResultDividedStringCodes.DIV_BY_THREE_AND_FIVE.value
    elif div_by_3:
        response.message = ResultMessageText.DIV_BY_THREE.value
        response.string_code = ResultDividedStringCodes.DIV_BY_THREE.value
    elif div_by_5:
        response.message = ResultMessageText.DIV_BY_FIVE.value
        response.string_code = ResultDividedStringCodes.DIV_BY_FIVE.value
    return render_template('index_denominator.html', form=form, response=response)
