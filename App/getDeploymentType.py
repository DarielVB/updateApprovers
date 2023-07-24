import requests

def getDeploymentType(Authorization, team_prefix, endpoint):
    r = requests.get(endpoint + 'data-team-mngr/V1/Utilities/deployment-types/', 
                 headers={'Authorization': Authorization})
    print(r)
    print(team_prefix)
    json = r.json()
    for deployment_type in json["DeploymentsTypes"]:
        if(team_prefix == deployment_type["prefix"]):
            return deployment_type["id"], deployment_type["prefix"]
    return "nn"
