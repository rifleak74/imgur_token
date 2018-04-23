#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:53:30 2018

@author: cheating
"""

from imgurpython import ImgurClient



def get_input(string):
    return input(string)


def authenticate():
    # Get client ID and secret from config.py
    client_id = '44a97a3ff8f5b15'
    client_secret = '068d53884b44e0d84b046786f2cf88f957db9787'
    client = ImgurClient(client_id, client_secret)

    # Authorization flow, pin example (see docs for other auth types)
    authorization_url = client.get_auth_url('pin')

    print("Go to the following URL: {0}".format(authorization_url))

    # Read in the pin, handle Python 2 or 3 here.
    pin = get_input("Enter pin code: ")

    # ... redirect user to `authorization_url`, obtain pin (or code or token) ...
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

    print("Authentication successful! Here are the details:")
    print("   Access token:  {0}".format(credentials['access_token']))
    print("   Refresh token: {0}".format(credentials['refresh_token']))

    return client


# If you want to run this as a standalone script, so be it!
if __name__ == "__main__":
    authenticate()