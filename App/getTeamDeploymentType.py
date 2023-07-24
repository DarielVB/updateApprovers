import requests

def getTeamDeploymentType(Authorization, team_id, deployment_id, endpoint):
    r = requests.get(
        endpoint +'data-team-mngr/V1/Utilities/team-deployment-type?query=idTeam = '+str(team_id)+' AND idDeploymentType = '+str(deployment_id), 
                 headers={'Authorization': Authorization})
    json = r.json()
    return json["teamDeploymentTypes"][0]["interested"], json["teamDeploymentTypes"][0]["approvers"]