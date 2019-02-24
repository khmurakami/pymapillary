from pymapillary import Mappilary


map = Mappilary("insert client id here")

bbox = "16.430300,7.241686,16.438757,7.253186"
closeto = "13.0006076843,55.6089295863"
end_time = "2016-03-14T13:44:37.206Z"
image_keys = "LwrHXqFRN_pszCopTKHF_Q, Aufjv2hdCKwg9LySWWVSwg"
lookat= "12.9981086701,55.6075236275"
pano = "true" #or "false" it has to be lower cased
per_page = 1
project_keys="HvOINSQU9fhnCQTpm0nN7Q" #json is userkey this worked too? PSaXX2JB7snjFyHJF-Rb1A for sequence key? JnLaPNIam8LFNZL1Zh9bPQ all keys work?
radius=100
sequence_keys="PSaXX2JB7snjFyHJF-Rb1A, LMlIPUNhaj24h_q9v4ArNw"
start_time = "2016-03-14T13:44:37.206Z" #start_time" must be a valid ISO 8601 date
userkeys = "HvOINSQU9fhnCQTpm0nN7Q"
usernames = "maning"

print(map.search_images(bbox,))
