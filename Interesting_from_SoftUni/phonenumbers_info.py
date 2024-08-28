import phonenumbers            #pip install phonenumbers
from phonenumbers import geocoder, timezone, carrier

number = '+359882555445'

ch_number = phonenumbers.parse(number)
time_zone = timezone.time_zones_for_number(ch_number)
print(time_zone)

ch_number = phonenumbers.parse(number, region='CH')
print(geocoder.description_for_number(ch_number, lang='en'))

ch_number = phonenumbers.parse(number, region='RO')
print(carrier.name_for_number(ch_number, lang='en'))

# дава информация за телефонен номер