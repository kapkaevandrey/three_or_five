from os import environ


MESSAGE_RESPONSE = {
    'divided by three': 'Ой, ей ваше число делится 3',
    'divided by five': 'Ой, ей ваше число делится на 5',
    'divided by three and five': 'Ой, ей ваше число делится и на 3 и на 5',
    'no divided by three or five': 'К сожалению это число не делится ни на 3 ни на 5. Звоните Заку.'
}


class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
