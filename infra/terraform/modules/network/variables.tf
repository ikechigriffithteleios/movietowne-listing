variable "name" {
  description = "Prefix for resource naming"
  type        = string
}

variable "cidr_block" {
  description = "VPC CIDR block"
  type        = string
}

variable "private_subnets" {
  description = "Map of AZ to CIDR block for private subnets"
  type        = map(string)
}

variable "public_subnets" {
  description = "Map of AZ to CIDR block for public subnets"
  type        = map(string)
}

variable "tags" {
  description = "Base tags"
  type        = map(string)
  default     = {}
}
