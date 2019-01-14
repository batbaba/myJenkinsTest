import boto3
# prd = boto3.session.Session(profile_name='pharmacollective/pharmacollective-prd/admin')
# client =  boto3.client('stepfunctions')

# response = client.list_state_machines(
#     maxResults=123,
#     nextToken='string'
# )
# print(response)

# aws stepfunctions list-executions --state-machine-arn arn:aws:states:eu-west-1:340298264685:stateMachine:CustomDomainStateMachine --profile pharmacollective/pharmacollective-prd/admin

def role_arn_to_session(**args):
    """
    Usage :
        session = role_arn_to_session(
            RoleArn='arn:aws:iam::012345678901:role/example-role',
            RoleSessionName='ExampleSessionName')
        client = session.client('sqs')
    """
    client = boto3.client('sts')
    response = client.assume_role(**args)
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'])

mySession = role_arn_to_session(
    RoleArn = 'arn:aws:iam::340298264685:role/cloudar_assume_admin',
    RoleSessionName = 'test',
    SerialNumber = 'arn:aws:iam::432886151732:mfa/batbaba',
    TokenCode = '964039')

client = mySession.client('stepfunctions')
print(client.list_executions(stateMachineArn='arn:aws:states:eu-west-1:340298264685:stateMachine:CustomDomainStateMachine'))
#https://boto3.readthedocs.io/en/latest/reference/services/sts.html#STS.Client.get_session_token
#https://gist.github.com/daidokoro/44255154d2c032ed69796d3565f10171