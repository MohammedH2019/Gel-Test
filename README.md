# Remove Exif metadata from images

A small project that removes Exif metadata from images that are stored in an s3 bucket. The new updated image will be stored in another s3 bucket.

## Installation

Use the Dockerfile to build and run the python application.

```bash
docker build -t remove-exif
```
```bash
docker run -d remove-exif