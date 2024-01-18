import os
import requests
import re
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def get_access_token():
    data = {
        "grant_type": "refresh_token",
        "client_id": "rhsm-api",
        "refresh_token": os.getenv("OFFTOKEN")
    }
    try:
        r = requests.post(url="https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token", data=data)
        r.raise_for_status()
        return r.json().get("access_token")
    except requests.exceptions.RequestException as request_error:
        print(f"Error refreshing access token: {request_error}")
        return None
    except Exception as e:
        print(f"Error getting access token: {e}")
        return None

def errata(advisoryid, headers):
    r = requests.get(url=f"https://api.access.redhat.com/management/v1/errata/{advisoryid}", headers=headers)
    return r.json()

def errata_all(headers):
    access_token = get_access_token()

    if access_token is None:
        print("Error retrieving access token.")
        return None

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    try:
        r = requests.get(url="https://api.access.redhat.com/management/v1/errata", headers=headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as request_error:
        print(f"Error retrieving errata data: {request_error}")
        return None
    except Exception as e:
        print(f"Error processing errata data: {e}")
        return None

def search_and_print_rhea_advisories():
    access_token = get_access_token()

    if access_token is None:
        print("Error retrieving access token.")
        return

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    advisories = errata_all(headers)

    if advisories is None:
        print("Error retrieving advisories data.")
        return

    try:
        advisory_id_pattern = re.compile(r'RHEA-\d+:\d+')
        rhea_advisories = [advisory for advisory in advisories['body'] if advisory_id_pattern.match(advisory.get('advisoryId', ''))]

        if rhea_advisories:
            for advisory in rhea_advisories:
                publish_date = advisory.get('publishDate')
                if publish_date:
                    if isinstance(publish_date, int):
                        formatted_publish_date = datetime.utcfromtimestamp(publish_date).strftime('%Y-%m-%d %H:%M:%S UTC')
                    elif isinstance(publish_date, str):
                        formatted_publish_date = datetime.strptime(publish_date, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S UTC')
                    else:
                        formatted_publish_date = "N/A"
                else:
                    formatted_publish_date = "N/A"

                print(f"Advisory ID: {advisory['advisoryId']}")
                print(f"Type: {advisory['type']}")
                print(f"Synopsis: {advisory['synopsis']}")
                print(f"Publish Date: {formatted_publish_date}")
                print(f"Details: {advisory['details']}")
                print("\n" + "-"*50 + "\n")
        else:
            print("No RHEA advisories found.")
    except requests.exceptions.RequestException as request_error:
        print(f"Error making requests to the API: {request_error}")
    except Exception as e:
        print(f"Error processing advisories data: {e}")

if __name__ == "__main__":
    search_and_print_rhea_advisories()