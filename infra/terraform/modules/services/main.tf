terraform {
  required_version = ">= 1.6.0"
}

resource "aws_ecs_cluster" "this" {
  name = "${var.name}-cluster"
  tags = var.tags
}

resource "aws_ecs_task_definition" "service" {
  for_each               = var.services
  family                 = "${var.name}-${each.key}"
  network_mode           = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                    = each.value.cpu
  memory                 = each.value.memory
  execution_role_arn     = var.execution_role_arn
  task_role_arn          = var.task_role_arn

  container_definitions = jsonencode([
    {
      name      = each.key
      image     = each.value.image
      essential = true
      portMappings = [
        {
          containerPort = each.value.port
          hostPort      = each.value.port
          protocol      = "tcp"
        }
      ]
      environment = [for k, v in merge(var.common_env, each.value.env) : {
        name  = k
        value = v
      }]
    }
  ])
}
