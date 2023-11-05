terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
  provider "aws" {
    region = "us-east-1"
  }
  locals {
    project_name = "Kosta"
  }
}

resource "aws_s3_bucket" "kosta_bucket" {
  bucket = "kosta-bucket-from-tf"
}