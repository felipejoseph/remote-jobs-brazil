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
  
  subnet_id               = "subnet-099feb3735a0ec3d3" 
  associate_public_ip_address = true          
  security_groups         = ["sg-0c076607883a4a464"]

  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file(env("AWS_PEM"))
    host        = self.public_ip
  } 

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",          # Atualiza os pacotes
      "sudo amazon-linux-extras install -y docker",  # Instala o Docker
      "sudo service docker start",   # Inicia o serviço do Docker
      "sudo usermod -aG docker ec2-user"  # Adiciona o usuário ec2-user ao grupo docker
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