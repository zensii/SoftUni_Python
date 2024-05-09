import phonenumbers
from phonenumbers import geocoder, carrier
#  from python_basics.location import geolocation


def get_phone_info(search_phone_number):
    parsed_number = phonenumbers.parse(search_phone_number, region=None)
    country = geocoder.description_for_number(parsed_number, lang='en')
    carrier_name = carrier.name_for_number(parsed_number, lang='en')

    print('Phone number:', search_phone_number)
    print('Country', country)
    print('Carrier:', carrier_name)
#    print(geolocation())


phone_number = '+359888501523'
get_phone_info(phone_number)
