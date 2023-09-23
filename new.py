import phonenumbers
from phonenumbers import geocoder
import folium

Key = "db2d940b6a9a458db49341d4e02647b9"

number = input("Masukkan Nomor anda dengan code +")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, 'en')
print(number_location)


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))


from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)


query = str(number_location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)


map_location = folium.Map(location = [lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")