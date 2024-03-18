# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build

absolute_path = os.path.dirname(__file__)
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyA--pIkKHQh4liTYnEJnRxFx_8HiZOQ-qM"
    # Get credentials and create an API client
    
    youtube = build(api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="cafe music"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()