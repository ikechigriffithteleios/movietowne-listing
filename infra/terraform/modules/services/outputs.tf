output "cluster_id" {
  description = "ECS cluster ID"
  value       = aws_ecs_cluster.this.id
}

output "task_definition_arns" {
  description = "Task definition ARNs"
  value       = { for k, v in aws_ecs_task_definition.service : k => v.arn }
}
