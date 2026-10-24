# RabbitMQ Exchange & Routing topology for Occupify RPC

RPC_EXCHANGE = "occupify.agent.rpc"

# Helper for routing key and queue conventions:
# routing key: <service>.<entity>.<verb> (e.g. core.job.get)
# queue: occupify.<service>.rpc.<entity>.<verb> (e.g. occupify.core.rpc.job.get)


def queue_name_for(routing_key: str) -> str:
    parts = routing_key.split(".", 1)
    if len(parts) == 2:
        service, rest = parts
        return f"occupify.{service}.rpc.{rest}"
    return f"occupify.rpc.{routing_key}"
