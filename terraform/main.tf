terraform {
  required_providers {
    aws ={
        source = "hashicorp/aws"
        version = "~> 4.16"
    }
  }
  required_version = ">=1.2.0"

}
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "comentarios-app" {
  ami           = "ami-01e82af4e524a0aa3" 
  instance_type = "t2.micro"               
  key_name      = "iac-teste"     

  tags = {
    Name = "comentarios-api"
  }
  
  provisioner "remote-exec" {
    inline = [
      "sudo yum install -y docker",
      "sudo service docker start"
    ]
  }
}
resource "aws_route53_record" "comentarios-app_dns" {
  zone_id = "Z08547862T01532USN2TQ"  
  name    = "comentarios.felipestestes.net"      
  type    = "A"
  ttl     = "300"
  records = [aws_instance.comentarios-app.public_ip]
  allow_overwrite = true
}