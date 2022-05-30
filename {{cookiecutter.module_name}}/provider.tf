provider "aws" {
  region                      = "us-east-1"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  s3_force_path_style         = true
  skip_requesting_account_id  = true
  skip_get_ec2_platforms      = true
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
  endpoints {
    s3 = "http://localhost:4566"
  }
}
