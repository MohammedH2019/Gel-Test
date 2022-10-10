locals{
    tags = {
    "project"     = "gls"
    "region"      = "eu-west-1"
    "environment" = "test"
    "owner"       = "Mohammed Hoche"
    "live"        = "no"
  }
  name_s3 = [
    "mh-input-bucket-first",
    "mh-output-bucket-first",
  ]
}
