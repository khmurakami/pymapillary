from error_handling import *

import requests
import wget

class Mappilary():

    def __init__(self, client_id):

        if client_id is None:
            raise Exception("No Client id inserted")

        self.root_url = "https://a.mapillary.com/v3"
        self.client_id = client_id

    # https://www.mapillary.com/developer/api-documentation/#pagination
    def get_pagnation_resources(self, page_num=1, per_page=200):

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
    def search_images(self, bbox=None, closeto=None, end_time=None,
                      image_keys=None, lookat=None, pano="false", per_page=200,
                      project_keys=None, radius=100, sequence_keys=None,
                      start_time=None, userkeys=None, usernames=None):

        """
        Search images by parameter
        """

        url = self.root_url + "/images"

        data = {
                 'bbox': bbox,
                 'closeto': closeto,
                 'end_time': end_time,
                 'image_keys': image_keys,
                 'pano': pano,
                 'per_page': per_page,
                 'radius': radius,
                 'sequence_keys': sequence_keys,
                 'start_time': start_time,
                 'userkeys': userkeys,
                 'usernames': usernames,
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

        url = self.root_url + "/images/" + key

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_image_detections(self, bbox=None, closeto=None, image_keys=None,
                                layers=None, max_score=None, min_score=None,
                                per_page=200, radius=50, userkeys=None,
                                usernames=None, values=None):

        """
        get image detections
        """

        url = self.root_url + "/image_detections"

        data = {
                 'bbox': bbox,
                 'closeto': closeto,
                 'image_keys': image_keys,
                 'layers': layers,
                 'max_score': max_score,
                 'min_score': min_score,
                 'per_page': per_page,
                 'radius': radius,
                 'userkeys': userkeys,
                 'usernames': usernames,
                 'values': values,
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_sequences(self, bbox=None, end_time=None, per_page=200,
                         starred="false", start_time=None, userkeys=None,
                         usernames=None):

        """
        search sequences
        """

        url = self.root_url + "/sequences"

        data = {
                 'bbox': bbox,
                 'end_time': end_time,
                 'per_page': per_page,
                 'starred': starred,
                 'start_time': start_time,
                 'userkeys': userkeys,
                 'usernames': usernames,
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

        url = self.root_url + "/sequences/" + key

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_changesets(self, bbox=None, per_page=200, states=None,
                          types=None, userkeys=None):

        """
        search changesets
        """

        url = self.root_url + "/changesets"

        data = {
                 'bbox': bbox,
                 'per_page': per_page,
                 'states': states,
                 'types': types,
                 'userkeys': userkeys,
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

        url = self.root_url + "/changesets/" + key

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_map_features(self, bbox=None, closeto=None, layers=None,
                            max_nbr_image_detections=None,
                            min_nbr_image_detections=None, per_page=200
                            radius=100, userkeys=None, usernames=None,
                            values=None):

        """
        search map features
        """

        url = self.root_url + "/map_features"

        data = {
                 'bbox': bbox,
                 'closeto': closeto,
                 'layers': layers,
                 'max_nbr_image_detections': max_nbr_image_detections,
                 'min_nbr_image_detections': min_nbr_image_detections,
                 'per_page': per_page,
                 'radius': radius,
                 'userkeys': userkeys,
                 'usernames': usernames,
                 'values': values,
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def search_users(self, bbox=None, per_page=200, userkeys=None,
                     usernames=None):

        """
        search users
        """

        url = self.root_url + "/users"

        data = {
                 'bbox': bbox,
                 'per_page': per_page,
                 'userkeys': userkeys,
                 'usernames': usernames,
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

        url = self.root_url + "/users/" + key

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

        url = self.root_url + "/users/" + key + "/stats"

        data = {
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json

    def filter_image_upload_lboards(self, bbox=None, end_time=None,
                                    iso_countries=None, per_page=200,
                                    start_time=None, userkeys=None,
                                    usernames=None):

        """
        filter leaderboards on image upload
        """

        url = self.root_url + "/leaderboard/images"

        data = {
                 'bbox': bbox,
                 'end_time': end_time,
                 'iso_countries': iso_countries,
                 'per_page': '{}'.format(per_page),
                 'start_time': start_time,
                 'userkeys': userkeys,
                 'usernames': usernames,
                 'client_id': '{}'.format(self.client_id)
                }

        r = requests.get(url, params=data)
        http_error_handler(r.status_code)
        raw_json = r.json()
        return raw_json



if __name__ == "__main__":
    map = Mappilary("SVdKb0JXclRud1I0NGFTbTNnWXNBQTphYTI5MDEwOGRlZmYzNTI3")
    print(map.search_images(usernames="maning"))
