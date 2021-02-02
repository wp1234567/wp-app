from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
import json
from math import radians, asin, cos, sin
from math import sqrt

def get_londoners():  # noqa: E501
    """get_londoners

    :rtype: None
    """
    api_instance = swagger_client.DefaultApi(swagger_client.ApiClient())

    try:
        users = api_instance.get_users()
        londoners = api_instance.get_users_by_city("London")
        
        # Retrieve the list of users within 50 miles from London and add them to the list of London users
        london_users = londoners
        for user in range(len(users)):
            lat = radians(float(users[user]["latitude"]))
            long = radians(float(users[user]["longitude"]))
            
            if distance_from_london(lat, long) <= 50:
                london_users.append(users[user])
        
        london_users = [dict(d) for d in{tuple(user.items()) for user in london_users}]
        
    except ApiException as e:
        print("Exception when calling DefaultApi->get_users: %s\n" % e)

    return (london_users)

def distance_from_london(lat, long) -> int:
    
    # Earth's radius in miles
    radius = 3956
    
    # London's coordinates in radians
    lon_lat = radians(51.5074)
    lon_long = radians(0.1278)
    
    # Calculate angle subtended by the arch between London and the given coordinates
    subtended_angle = 2*asin(sqrt(sin((lat - lon_lat) / 2)**2 + cos(lon_lat) * cos(lat) * sin((long - lon_long) / 2)**2))
    
    # Return distance from London
    return radius * subtended_angle