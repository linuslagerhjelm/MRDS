import httplib
import json
from exception import FailedToGetException
from exception import FailedToPostException

HEADERS = {"Content-type": "application/json", "Accept": "text/json"}


class Mrdsapi:
    """Mrdsapi specifies a wrapper class around the api for a running mrds server

        Attributes:
            address: the web address to connect to
            port: the port to use for the connection
            url: the connection string to use when opening a connection
    """
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.url = address + ":" + str(port)

    def _request_data(self, url):
        """Perform the actual request to the external api. Return loaded json data"""
        connection = httplib.HTTPConnection(self.url)
        connection.request("GET", url)
        response = connection.getresponse()

        if response.status != 200:
            raise FailedToGetException.FailedToGetException(response.reason)

        data = response.read()
        response.close()

        return json.loads(data)

    def _post_data(self, url, data):
        """Performs a post request to the server with the specific data"""
        connection = httplib.HTTPConnection(self.url)
        json_data = json.dumps(data)
        connection.request("POST", url, json_data, HEADERS)
        response = connection.getresponse()

        if response.status != 204:
            raise FailedToPostException.FailedToPostException(response.reason)

        return response.status

    def get_localization(self):
        """Get the robots position from the API. Returns a Pose object"""
        return self._request_data("/lokarria/localization")

    def get_laser_echoes(self):
        """Get the current laser scan from the robot. Returns a dictionary containing laser data"""
        return self._request_data("/lokarria/laser/echoes")

    def get_laser_properties(self):
        """Get the laser properties from the Robot. Returns a dictionary containing laser data"""
        return self._request_data("/lokarria/laser/properties")

    def post_speed(self, angular, linear):
        """Posts the values for angular and linear speed to the robot"""
        data = {'TargetAngularSpeed': angular, 'TargetLinearSpeed': linear}
        return self._post_data("/lokarria/differentialdrive", data)
