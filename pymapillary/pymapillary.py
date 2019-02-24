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

    def search_image_detections(self, layers, per_page):

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
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_sequences(self, userkeys):

        """
        search sequences
        """

        url = self.root_url + "/sequences"

        data = {
                 'userkeys': "{}".format(userkeys),
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def get_sequence_by_key(self, key):

        """
        get a sequence by key
        """

        url = self.root_url + "/sequences/" + str(key)

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_changesets(self, types, per_page):

        """
        search changesets
        """

        url = self.root_url + "/changesets"

        data = {
                 'types': '{}'.format(types),
                 'per_page': '{}'.format(per_page),
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def get_changeset_by_key(self, key):

        """
        get a changeset by key
        """

        url = self.root_url + "/changesets/" + str(key)

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_map_features(self, layers, per_page):

        """
        search map features
        """

        url = self.root_url + "/map_features"

        data = {
                 'layers': '{}'.format(layers),
                 'per_page': '{}'.format(per_page),
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_users(self, per_page):

        """
        search users
        """

        url = self.root_url + "/users"

        data = {
                 'per_page': '{}'.format(per_page),
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def get_user_by_key(self, key):

        """
        get a user by key
        """

        url = self.root_url + "/users/" + str(key)

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def get_user_stats_by_key(self, key):

        """
        get a user by key
        """

        url = self.root_url + "/users/" + str(key) + "/stats"

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def filter_image_upload_lboards(self, per_page):

        """
        filter leaderboards on image upload
        """

        url = self.root_url + "/leaderboard/images"

        data = {
                 'per_page': '{}'.format(per_page),
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json



if __name__ == "__main__":
    map = Mappilary("")
    print(map.filter_image_upload_lboards(1))
