provider "aws" {
      region = "ap-south-1"
      access_key = "nmmmn"
      secret_key = "mnj,nn"
}

# Create a VPC
resource "aws_vpc" "prod-vpc" {
  cidr_block = "10.0.0.0/16"
  instance_tenancy = "default"
  tags = {
    Name = "prod-vpc"
  }
}

resource "aws_subnet" "prod-subnet-public-1" {
  cidr_block = "10.0.1.0/24"
  vpc_id = aws_vpc.prod-vpc.id
  availability_zone = "ap-south-1a"
  tags = {
    Name = "public-subnet"
  }
}


resource "aws_internet_gateway" "prod-igw" {
  vpc_id = aws_vpc.prod-vpc.id
  tags = {
    Name = "prod-igw"
  }
}

resource "aws_route_table" "prod-public-crt" {
  vpc_id = aws_vpc.prod-vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.prod-igw.id
  }
  tags = {
    Name: "prod-public-crt"
  }
}

resource "aws_route_table_association" "prod-crta-public-subnet-1" {
  route_table_id = aws_route_table.prod-public-crt.id
  subnet_id = aws_subnet.prod-subnet-public-1.id
}

resource "aws_security_group" "ssh-allowed" {
  vpc_id = aws_vpc.prod-vpc.id
  ingress {
    from_port = 22
    protocol = "tcp"
    to_port = 22
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = 80
    protocol = "tcp"
    to_port = 80
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
        Name = "ssh-allowed"
    }
}

resource "aws_instance" "web1" {
  ami = "ami-0e34af9d3686f9ace"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.prod-subnet-public-1.id
  security_groups = [aws_security_group.ssh-allowed.id]
  key_name = "By_Terraform_key"
  associate_public_ip_address = "true"
  tags = {
    Name = "My-Web"
  }
}
