terraform {
  backend "s3" {
    profile        = "X"
    bucket         = "gel-test-fstate"
    key            = "gel.tfstate"
    region         = "eu-west-1"
  }
}
provider "aws" {
  profile = "X"
  region  = "eu-west-1"
}