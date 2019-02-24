from pymapillary import Mapillary

map = Mapillary("SVdKb0JXclRud1I0NGFTbTNnWXNBQTphYTI5MDEwOGRlZmYzNTI3")

# Every parameter that can be passed in to this search function
# Plug and play as you please
bbox = "16.430300,7.241686,16.438757,7.253186" # minx,miny,maxx,maxy
closeto = "13.0006076843,55.6089295863" #longitude, latitude
end_time = "2016-03-14T13:44:37.206Z" #must be a valid ISO 8601 date
image_keys = "LwrHXqFRN_pszCopTKHF_Q, Aufjv2hdCKwg9LySWWVSwg"
lookat= "12.9981086701,55.6075236275" #longitude, latitude
pano = "true" # or "false" it has to be lower cased
per_page = 200 # defauly it 200
project_keys="HvOINSQU9fhnCQTpm0nN7Q" #json is userkey this worked too? PSaXX2JB7snjFyHJF-Rb1A for sequence key? JnLaPNIam8LFNZL1Zh9bPQ all keys work?
radius=100 # In meters
sequence_keys="PSaXX2JB7snjFyHJF-Rb1A, LMlIPUNhaj24h_q9v4ArNw"
start_time = "2016-03-14T13:44:37.206Z" #start_time" must be a valid ISO 8601 date
userkeys = "HvOINSQU9fhnCQTpm0nN7Q"
usernames = "maning" #example user name

raw_json = map.search_images(bbox=bbox, per_page=1)
print(raw_json)

# Result JSON
"""
{u'type': u'FeatureCollection', u'features': [{u'geometry': {u'type': u'Point', u'coordinates': [16.432976, 7.249027]}, u'type': u'Feature', u'properties': {u'username': u'pierregeo', u'sequence_key': u'LMlIPUNhaj24h_q9v4ArNw', u'camera_make': u'Apple', u'user_key': u'AGfe-07BEJX0-kxpu9J3rA', u'ca': 329.94820000000004, u'camera_model': u'iPhone5,4', u'key': u'G_SIwxNcioYeutZuA8Rurw', u'pano': False, u'captured_at': u'2016-03-14T13:45:45.849Z'}}]}
"""
