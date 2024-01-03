
resource "aws_s3_bucket" "kosta_bucket" {
  bucket = "kosta-bucket-from-tf"
}

resource "aws_s3_bucket" "kosta_bucket_testing_for_state_migration" {
  bucket = "kosta_bucket_testing_for_state_migration"
}