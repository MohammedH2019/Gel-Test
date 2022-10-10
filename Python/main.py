import boto3
from PIL import Image
# connecting to the AWS Bucket
s3 = boto3.resource('s3') 
bucket = s3.Bucket('mh-input-bucket-first')
destination_bucket = "mh-output-bucket-first"


# push new image without metadata to the destination bucket
def upload_images(new_images):
    for new_image in range(len(new_images)):
        print(new_images[new_image])
        s3_client = boto3.client('s3')
        s3_client.upload_file(new_images[new_image], destination_bucket,new_images[new_image]) 

# removing the metadata from the image
def image_exif_removal(image_list):
    images_without_exif = [] # new array to store new images without metadata
    for image in range(len(image_list)):
        print(image_list[image])
        image1 = Image.open(image_list[image])
        data = list(image1.getdata())
        image_remove_exif = Image.new(image1.mode, image1.size)
        image_remove_exif.putdata(data)
        image_remove_exif.save(image_list[image])
        images_without_exif.append(image_list[image])
    upload_images(images_without_exif)    

# grabbing all the obj/images  in the source bucket
def bucket_images():
    images = [] # array to store the images
    for obj in bucket.objects.all():
        s3.meta.client.download_file(str(bucket.name),obj.key, obj.key)
        images.append(obj.key)
    print(images) 
    image_exif_removal(images)   


bucket_images()