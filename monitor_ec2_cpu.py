import boto3
from detetime import detetime, timedelta
#create cloudwatch client 
cloudwatch = boto3.client("cloudwatch" , region_name = "us-east-1")
INSTANCE_ID = "EC2 ID" #here we put id for monitor 

#Get CPU utilization
response = cloudwatch.get_metric_statistics(
    Namespace = "AWS/EC2",
    MetricName = "CPUUtilization",
    Dimensions = [
        {
            "Name":"InstanceID",
            "Value": INSTANCE_ID
        }
    ],
    StartTime= datetime.utcnow()-timedelta(minutes=10),
    EndTime= datetime.utcnow(),
    Period = 300,
    statistics = ["Average"]
)
if response ["Datapoints"]:
    cpu_usage = response["Datapoints"][0]["Average"]
    print(f"CPU Usage for {INSTANCE_ID}:{cpu_usage:.2f}%")

    if cpu_usage > 70:
        print("ALERT: High CPU usage")
    else:
        print("No data available")