terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.0.0"
}

provider "aws" {
  region  = "us-west-2"
}

resource "aws_instance" "comentarios_app" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"
  key_name = "iac-teste"
  
  tags = {
    Name = "comentarios-app-instance"
  }
  
}
output "public_ip" {
  value = aws_instance.comentarios_app.public_ip
}