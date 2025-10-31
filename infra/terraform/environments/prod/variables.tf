variable "region" {
  description = "AWS region"
  type        = string
}

variable "vpc_cidr" {
  description = "VPC CIDR"
  type        = string
}

variable "private_subnets" {
  description = "Private subnet CIDRs"
  type        = map(string)
}

variable "public_subnets" {
  description = "Public subnet CIDRs"
  type        = map(string)
}

variable "execution_role_arn" {
  description = "ECS execution role ARN"
  type        = string
}

variable "task_role_arn" {
  description = "ECS task role ARN"
  type        = string
}

variable "database_url" {
  description = "Database connection string"
  type        = string
}

variable "redis_url" {
  description = "Redis connection string"
  type        = string
}

variable "common_env" {
  description = "Additional environment variables"
  type        = map(string)
  default     = {}
}

variable "services" {
  description = "Service definitions"
  type = map(object({
    cpu    = string
    memory = string
    image  = string
    port   = number
    env    = map(string)
  }))
}

variable "tags" {
  description = "Base tags"
  type        = map(string)
  default     = {}
}
