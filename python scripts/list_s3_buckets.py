import boto3

session = boto3.Session(
    aws_access_key_id="AKIARPN7B4NBXMGYACO2",
    aws_secret_access_key="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",
)

#to list all s3 buckets
def list_my_buckets(s3_resource):
    print('Buckets:\n\t', *[b.name for b in s3_resource.buckets.all()], sep="\n\t")
    
s3_resource = (
    boto3.resource('s3', region_name="ap-south-1") 
)

#to list all ec2's
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print("Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
        ,instance.private_ip_address)
     )


#to get all the contents inthe bucket
my_bucket = s3_resource.Bucket('dev-thors3bucket')
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)


list_my_buckets(s3_resource)