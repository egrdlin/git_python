import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocodi16ng/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        address = input('Enter location: ')
        if len(address) < 1: break

        parms = dict()
        parms['address'] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)

        data = uh.read()
        print('Retrieved', len(data), 'characters')
        # print(data.decode())
        tree = ET.fromstring(data)

        results = tree.findall('result')
        # lat = results[0].find('geometry').find('location').find('lat').text
        # lng = results[0].find('geometry').find('location').find('lng').text
        location = results[0].find('formatted_address').text

        # print('lat', lat, 'lng', lng)
        # print(location)

        all_address_components = tree.findall('result/address_component')
        # print('Address Components:', len(all_address_components))

        short_name = list()
        type_list = list()
        
        for item in all_address_components:
            # print('Long Name', item.find('long_name').text,"\n")
            # print('Short Name:', item.find('short_name').text, "\n")
            all_types = item.findall('type')
            short_name.append(item.find("short_name").text)

            for types in all_types:
                # print(types.text,"\n")
                type_list.append(types.text)

            # print('Type:', item.find('type').text, "\n")
        country = type_list[len(type_list)-2]
        # print(country)

        if(country == "country"):
            print("\n\n2 letter country code: ",short_name[len(short_name)-1])
        else:
            print("Entered address is: ",country, " type, therefore, no country code.") # handle non-country type address
        continue

    except Exception as e: # handle error
        print("Unrecognized location, retry")
        continue # re-enter