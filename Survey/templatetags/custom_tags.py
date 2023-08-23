from django import template
# Create your views here.
register = template.Library()

def concat_string(value):
    print("LOG:ENTER")
    print("Value:",value)
    return str(value.split()[0])

register.filter('modify_name', concat_string)