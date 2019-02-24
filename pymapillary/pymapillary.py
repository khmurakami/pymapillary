from error_handling import *

import requests
import wget

class Mappilary():

    def __init__(self, client_id):
        # Root URL of mapillaru calls

        if client_id is None:
            raise Exception("No Client id inserted")

        self.root_url = "https://a.mapillary.com/v3"
        self.client_id = client_id

    # https://www.mapillary.com/developer/api-documentation/#pagination
    def get_pagnation_resources(self, page_num, per_page):

        """
        Get pagnation Resources

        """

        url = self.root_url + "/sequences"

        data = {
                 'page' : '{}'.format(page_num),
                 'per_page' : '{}'.format(per_page),
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    #https://www.mapillary.com/developer/api-documentation/#search-images
    def search_images(self):

        """
        Search images by parameter
        """

        url = self.root_url + "/images"

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r)
        raw_json = r.json()
        return raw_json

    def get_image_feature(self, key):

        """
        Get a image feature by the key
        """

        url = self.root_url + "/images" + "/" + key

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def get_image_detections(self, layers, per_page):

        """
        get image detections
        """

        url = self.root_url + "/image_detections"

        data = {
                 'layers': "{}".format(layers),
                 #'bbox': "{}".format(layers),
                 'per_page': "{}".format(per_page),
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        print(r.status_code)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json




if __name__ == "__main__":
    map = Mappilary("")
    print(map.get_image_detections("trafficsigns", 2))
