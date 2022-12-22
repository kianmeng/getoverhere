import json

import requests


class ResolveRequests:
    def __init__(self, url, session, cookies=None, parameters=None):
        self.url = url
        self.session = session
        self.cookies = cookies
        self.parameters = parameters

        # TODO
        # If header is None, guess header content_type
        head = requests.head(self.url)
        if "Content-Type" in head.headers:
            type = head.headers["Content-Type"]
            self.headers = {"Content-Type": type}
        else:
            self.headers = None

    def resolve_get(self):
        response = self.session.get(
            self.url,
            json=self.parameters,
            headers=self.headers,
            cookies=self.cookies,
        )
        try:
            return [
                json.dumps(response.json(), indent=4),
                response.status_code,
            ]
        except requests.exceptions.JSONDecodeError:
            return [response.text, response.status_code]

    def resolve_post(self):
        response = self.session.post(
            self.url, json=self.parameters, headers=self.headers
        )
        try:
            return json.dumps(response.json(), indent=4)
        except requests.exceptions.JSONDecodeError:
            return response.text
