# RabbitMQ Exchange topology for Occupify RPC and Events

from faststream.rabbit import ExchangeType, RabbitExchange, RabbitQueue

RPC_EXCHANGE = "occupify.agent.rpc"
EVENT_EXCHANGE = "occupify.core.exchange"
JOB_SYNC_QUEUE = "occupify.agentic.job_sync"

events_exchange = RabbitExchange(EVENT_EXCHANGE, type=ExchangeType.TOPIC)
job_sync_queue = RabbitQueue(JOB_SYNC_QUEUE, routing_key="project.*")
job_item_queue = RabbitQueue("occupify.agentic.job_item_sync", routing_key="job.#")
