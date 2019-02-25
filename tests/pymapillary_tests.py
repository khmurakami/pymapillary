#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymapillary import Mapillary

import unittest
import os

class TestMapillaryMethods(unittest.TestCase):

    def test_get_pagnation_resources(self):
        map = Mapillary("SVdKb0JXclRud1I0NGFTbTNnWXNBQTphYTI5MDEwOGRlZmYzNTI3")

        page_num = 1
        per_page = 1

        raw_json = map.get_pagnation_resources(page_num=page_num,
                                               per_page=per_page)

        # Since the page can change, I just check if a request just went through
        features_json = raw_json['features']
        self.assertEqual(type([]), type(features_json))

    def test_search_images(self):
        map = Mapillary("SVdKb0JXclRud1I0NGFTbTNnWXNBQTphYTI5MDEwOGRlZmYzNTI3")

        bbox = "16.430300,7.241686,16.438757,7.253186"
        per_page = 1

        raw_json = map.search_images(bbox=bbox, per_page=per_page)
        features_json = raw_json['features']

        # The json's is in a list
        for features in features_json:
            coordinate = features['geometry']['coordinates']

        self.assertEqual([16.432976, 7.249027], coordinate)

    def test_get_image_feature_by_key(self):
        map = Mapillary("SVdKb0JXclRud1I0NGFTbTNnWXNBQTphYTI5MDEwOGRlZmYzNTI3")

        key = "LwrHXqFRN_pszCopTKHF_Q"

        raw_json = map.get_image_feature_by_key(key=key)

        properties_ca_angle = raw_json['properties']['ca']

        self.assertEqual(323.0319999999999, properties_ca_angle)

    def test_search_sequences(self):
        map = Mapillary("SVdKb0JXclRud1I0NGFTbTNnWXNBQTphYTI5MDEwOGRlZmYzNTI3")

        userkeys = "AGfe-07BEJX0-kxpu9J3rA"
        per_page = 1

        raw_json = map.search_sequences(userkeys=userkeys, per_page=per_page)
        type_json = raw_json['type']

        self.assertEqual("FeatureCollection", type_json)



if __name__ == '__main__':
    unittest.main()
