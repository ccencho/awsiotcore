import json
import boto3
import base64

client = boto3.client('iot-data', region_name='us-east-1')

def lambda_handler(event, context):
    print(event)
    payload = event['PayloadData']
    decoded = base64.b64decode(payload)

    #Bateria 
    #if decoded[0]==1 and decoded[1]==117:
    #    bate = decoded[2]
        
    #Temperatura    
    if decoded[0]==3 and decoded[1]==103:
        temp = ( decoded[3]<<8 | decoded[2] )/10.0
        
    #Humedad    
    if decoded[4]==4 and decoded[5]==104:
        humi = decoded[6] /2.0    
  
    response = client.publish(
        topic='em300/decoded',
        qos=1,
        payload=json.dumps({"device":"em300","temperatura":temp,'humedad':humi})
    )
    print(response)
  
    return {
 
        'temp': temp,
        'humi': humi,
        'statusCode': 200,
        'body': json.dumps('Published to topic')

    }
