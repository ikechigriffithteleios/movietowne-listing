terraform {
  required_version = ">= 1.6.0"
  backend "s3" {}
}

provider "aws" {
  region = var.region
}

module "network" {
  source          = "../../modules/network"
  name            = "movietowne-dev"
  cidr_block      = var.vpc_cidr
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets
  tags            = var.tags
}

module "services" {
  source             = "../../modules/services"
  name               = "movietowne-dev"
  execution_role_arn = var.execution_role_arn
  task_role_arn      = var.task_role_arn
  tags               = var.tags
  common_env = merge(
    {
      "ENVIRONMENT" = "development"
      "DATABASE_URL" = var.database_url
      "REDIS_URL"    = var.redis_url
    },
    var.common_env
  )
  services = var.services
}
