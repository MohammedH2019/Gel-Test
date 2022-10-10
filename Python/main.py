import boto3
from PIL import Image
# connecting to the AWS Bucket
s3 = boto3.resource('s3') 
bucket = s3.Bucket('mh-input-bucket-first')
destination_bucket = "mh-output-bucket-first"

for obj in bucket.objects.all(): # travesring thrugh every object in the input bucket
    print(obj.key) # grab first object
     # download the obj image
    s3.meta.client.download_file(str(bucket.name),obj.key, obj.key)
    image1 = Image.open(obj.key) 
    data = list(image1.getdata())
    #removing the metadata and saving the the image
    image_remove_exif = Image.new(image1.mode, image1.size) 
    image_remove_exif.putdata(data) 
    image_remove_exif.save(obj.key) 
    # push  the new image to the new bucket
    s3_client = boto3.client('s3')
    image_remove_exif.convert()
    s3_client.upload_file(obj.key, destination_bucket,obj.key) 


