#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import json
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

def main(dict):
    serviceUsername = "be4be6a3-1291-4fff-b5a5-ba96ec59cc51-bluemix"
    servicePassword = "eb20078854e388961048c140db57fdbcc0c9fa0202723dad1fc333249c48459e"
    serviceURL = "https://be4be6a3-1291-4fff-b5a5-ba96ec59cc51-bluemix:eb20078854e388961048c140db57fdbcc0c9fa0202723dad1fc333249c48459e@be4be6a3-1291-4fff-b5a5-ba96ec59cc51-bluemix.cloudant.com"
    databaseName = "wiam_db"
    
    #print(dict)
    
    client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
    client.connect()
    myDB = client[databaseName]
    
    end_point = '{0}/{1}'.format(serviceURL, 'wiam_db/_find')
    headers={'Content-Type': 'application/json'}
    params = {'include_docs': 'true'}
    data = '{"selector": {"wr_id":"'+str(dict['workid'])+'"}}'
    # Issue the request
    response = client.r_session.post(end_point, headers=headers, params=params, data=data)
    
    #check to see any docs have returned
    if(len(response.json()['docs'])==0):
        output_val={'status':'NODOCS'}
    else:
        output_val = {'status':response.json()['docs'][0]['status']}
    
    #print(output_val)
    
    # Display the response content
    return(output_val)
    
    