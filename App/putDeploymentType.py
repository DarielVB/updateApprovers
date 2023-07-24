import requests
import json
from requests.structures import CaseInsensitiveDict

def putDeploymentType(Authorization, team_id, deployment_id, interested, new_approvers, endpoint):
    data = {
    'Interested': interested,
    'Approvers': new_approvers
    }
    data_json = json.dumps(data)

    headers = CaseInsensitiveDict()
    headers["AUTHORIZATION"] = Authorization
    headers["Content-Type"] = "application/json"
    r = requests.put(endpoint +'data-team-mngr/V1/Utilities/team-deployment-type/teams/'+str(team_id)+'/deployment-types/'+str(deployment_id)+'',
                    headers=headers,
                     data = str(data_json))
    
    print(r.text)

    r2 = requests.get(
        endpoint + 'data-team-mngr/V1/Utilities/team-deployment-type?query=idTeam = '+str(team_id)+' AND idDeploymentType = '+str(deployment_id), 
                 headers={'Authorization': Authorization})
    dataupdate = r2.json()

    print("Team updated: "+str(dataupdate["teamDeploymentTypes"]))
    
    return dataupdate["teamDeploymentTypes"][0]["approvers"]