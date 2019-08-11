import boto3


cloudwatch = boto3.client('cloudwatch')
# client = boto3.client('elbv2')
# response = client.describe_load_balancers(
#     LoadBalancerArns=[
#         'arn:aws:elasticloadbalancing:ap-south-1:690379282706:loadbalancer/app/Test-NP-EXT-ELB/7b275a485b3abac0',
#     ],
# )

# print(response)