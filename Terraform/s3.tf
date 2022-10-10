resource "aws_s3_bucket" "gls_buckets" {
  for_each = toset(local.name_s3)
  bucket = each.key

  tags = local.tags
}
