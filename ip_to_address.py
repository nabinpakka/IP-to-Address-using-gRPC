import geoip2.database

def get_location_ip(ip):
    reader = geoip2.database.Reader("./GeoLite2-City_20190924/GeoLite2-City.mmdb")
    response = reader.city(ip)
    print(response.city.name)
    print(response.country.name)
    city = response.city.name
    country = response.country.name
    res = city +","+country

    reader.close()
    return res

# get_location_ip("45.64.161.176")