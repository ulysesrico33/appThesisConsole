import requests

url = "https://9de16523-0e36-4ff0-b388-44e8d0b1581f-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/thesis/tables/tbthesis/columns"

headers = {
    'accept': "application/json",
    'x-cassandra-token': "f896656d-4893-4c11-871b-c5ca7f271549",
    'x-cassandra-request-id': "094ce42d-ec7e-47b0-89cd-4ca395f043fb"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)