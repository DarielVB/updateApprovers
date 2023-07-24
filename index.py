import json
import utils.config
from App.getTeams import getTeams
from App.getDeploymentType import getDeploymentType
from App.getTeamDeploymentType import getTeamDeploymentType
from App.putDeploymentType import putDeploymentType

with open('json/aprobadores.json', 'r', encoding='utf-8') as f:
    print(utils.config.Endpoint)
    endpoint = utils.config.Endpoint
    my_list = json.load(f)
    index = 1
    for idx, team in enumerate(my_list):
        deploy_prefix = team["deploymentType"]["prefix"]
        deployment_id, deploy_got_prefix = getDeploymentType(utils.config.Authorization, deploy_prefix, endpoint)

        team_prefix = team["team"]["prefix"]
        team_id, team_name, team_got_prefix = getTeams(utils.config.Authorization, team_prefix, endpoint)
        print("equipo: "+team_prefix+ " prefix: "+deploy_prefix)
        if (deploy_prefix != deploy_got_prefix or team_prefix != team_got_prefix):
            print("\nERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR \n")
            print(team)
            print("\nERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR \n")
        else:
            interested, old_approvers = getTeamDeploymentType(utils.config.Authorization, team_id, deployment_id, endpoint)
            print(interested)
            new_approvers = team["approvers"]
            print(new_approvers)
            data3 = putDeploymentType(utils.config.Authorization, team_id, 
            deployment_id, interested, new_approvers, endpoint)
            print(data3)
            print(new_approvers)
            if new_approvers == data3:
                print("bien")
            else:
                print("Id del team = "+str(team_id)+" Id del prefix  = "+str(deployment_id))
                print("error")
    index = index+1
            
       