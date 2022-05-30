resource "aws_s3_bucket" "s3_bucket" {
  bucket = "test"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
