import requests
def pininfo(pincode):
    api_address = "https://api.postalpincode.in/pincode/"

    url = api_address+pincode
    try:
        json_data = requests.get(url).json()
        data = "Name: {0},DeliveryStatus: {1},Circle:{2},District:{3},Region:{4},State:{5}".format(
            json_data[0]['PostOffice'][0]['Name'],
            json_data[0]['PostOffice'][0]['DeliveryStatus'],
            json_data[0]['PostOffice'][0]['Circle'],
            json_data[0]['PostOffice'][0]['District'],
            json_data[0]['PostOffice'][0]['Region'],
            json_data[0]['PostOffice'][0]['State']
        )
    except:
        return "This pincode does not exists"

    return data
# print(pininfo("425201"))


def freefood(city):

    api_address = "http://ec2-3-23-130-174.us-east-2.compute.amazonaws.com:8000/resource?city={0}&category=Free%20Food".format(city)

    try:
        json_data = requests.get(api_address).json()
        data = "Service: {0},City:{1} ,website:{2}, Call-on:{3}, State:{4}, Description:{5}".format(
            json_data['data'][0]['category'],
            json_data['data'][0]['city'],
            json_data['data'][0]['contact'],
            json_data['data'][0]['phone'],
            json_data['data'][0]['state'],
            json_data['data'][0]['description']
        )
    except:
        return "API Calling Failed! Sorry Restart Chat"
    return data
# print(freefood("Mumbai"))

def service_detail(cityname, service):
    api_address = "http://ec2-3-23-130-174.us-east-2.compute.amazonaws.com:8000/resource?city={0}&category={1}".format(cityname, service)

    try:
        json_data = requests.get(api_address).json()
        data = "Service: {0},City:{1} ,website:{2}, Call-on:{3}, State:{4}, Description:{5}".format(
            json_data['data'][0]['category'],
            json_data['data'][0]['city'],
            json_data['data'][0]['contact'],
            json_data['data'][0]['phone'],
            json_data['data'][0]['state'],
            json_data['data'][0]['description']
        )
    except:
        return "Sorry. No service found in this city"
    return data

# print(service_detail("pune","fundraisers"))