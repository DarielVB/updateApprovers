import requests

def getTeams(Authorization, team, endpoint):
    r = requests.get(endpoint + 'data-team-mngr/V1/Utilities/teams/?query=prefix = '+team, 
                 headers={'Authorization': Authorization})
    json = r.json()
    return json["teams"][0]["id"], json["teams"][0]["name"], json["teams"][0]["prefix"]