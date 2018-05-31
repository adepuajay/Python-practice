from random import choice

def get_report():
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    report = choice(possibilities)
    return report
