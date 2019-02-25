from pymapillary import Mapillary

import unittest
import os

class TestMapillaryMethods(unittest.TestCase):

    def test_search_images(self):
        map = Mapillary("SVdKb0JXclRud1I0NGFTbTNnWXNBQTphYTI5MDEwOGRlZmYzNTI3")

        bbox = "16.430300,7.241686,16.438757,7.253186"
        per_page = 1

        raw_json = map.search_images(bbox=bbox, per_page=per_page)
        features_json = raw_json['features']

        # The json's is in a list
        for features in features_json:
            coordinate = features['geometry']['coordinates']
            print(coordinate)

        self.assertEqual([16.432976, 7.249027], coordinate)

if __name__ == '__main__':
    unittest.main()
