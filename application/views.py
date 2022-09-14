from application import app
from flask import render_template
from webargs.flaskparser import use_kwargs
from webargs import fields
from .utils import get_rates


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rates')
@use_kwargs(
    {
        'currency': fields.Str(required=True)
    },
    location='query'
)
def search_rates(currency):
    rates = get_rates()
    for i in rates:
        if i["code"] == currency or i["name"] == currency:
            rate = i
            return render_template('btc_rates_res.html', rate=rate)
