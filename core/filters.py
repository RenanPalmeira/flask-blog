# -*- coding: utf8 -*-
import datetime

def Filters(app):
    @app.template_filter('strftime')
    def _jinja2_filter_datetime(date):
        if type(date) is datetime.datetime:
            return date.strftime('%d/%m/%Y ás %Hh%Mm').decode('utf8')
        else: 
            d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            date = d.strftime('%d/%m/%Y ás %Hh%Mm').decode('utf8')
            return date
    @app.template_filter('item_count')
    def item_count(data,paramer):
        if str(paramer) in data:
            return data[str(paramer)]
        return 1

    @app.template_filter('money')
    def money(price):
        if price != '':
            price = str(price).replace(',', '.')
            price = float(price)
            price = format(price, ".2f")
            date = "R$ %s" % (str(price).replace('.', ','))
            return date
        return ''
