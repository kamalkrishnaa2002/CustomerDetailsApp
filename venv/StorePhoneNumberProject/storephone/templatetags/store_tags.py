from django import template

register = template.Library()

@register.simple_tag
def phone_links(store):
    if len(store.phone_number) == 10 or store.phone_number.startswith('91') or store.phone_number.startswith('+91'):
        if len(store.phone_number) == 11 and store.phone_number.startswith('91'):
            phone_number = store.phone_number[2:]  # Remove first two characters (91)
        elif store.phone_number.startswith('+91'):
            phone_number = store.phone_number[3:]  # Remove first three characters (+91)
        else:
            phone_number = store.phone_number

        call_link = f'<a href="tel:{store.phone_number}" id="phone{store.id}" onclick="hideStore({store.id})">Call {store.phone_number}</a>'
        whatsapp_link = f'<a href="https://wa.me/{phone_number}" target="_blank">WhatsApp {phone_number}</a>'

        return f'{call_link}<br>{whatsapp_link}'
    else:
        return f'Phone number has been clicked.'
