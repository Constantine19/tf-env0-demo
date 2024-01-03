
variable "s3_bucket_name" {
  type    = "list"
  default = ["kosta_1", "kosta_2"]
}

resource "aws_s3_bucket" "henrys_bucket" {
  count         = "${length(var.s3_bucket_name)}"
  bucket        = "${element(var.s3_bucket_name, count.index)}"
}