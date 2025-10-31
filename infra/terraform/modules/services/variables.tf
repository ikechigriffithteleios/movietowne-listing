variable "name" {
  description = "Environment name"
  type        = string
}

variable "tags" {
  description = "Resource tags"
  type        = map(string)
  default     = {}
}

variable "execution_role_arn" {
  description = "ECS execution role"
  type        = string
}

variable "task_role_arn" {
  description = "ECS task role"
  type        = string
}

variable "common_env" {
  description = "Common environment variables"
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
