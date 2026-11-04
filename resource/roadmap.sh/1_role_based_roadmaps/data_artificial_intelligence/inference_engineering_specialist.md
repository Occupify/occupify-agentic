# Inference Engineering Specialist

## Metadata
- Type: Role
- Domain: Data & Artificial Intelligence
- Source: roadmap.sh
- Source URL: https://roadmap.sh/inference-engineering
- Related Roles:
  - AI Engineer
  - Backend Developer
  - MLOps Engineer
  - DevOps Engineer

---

## 1. Beginner

### 1.1 Introduction
- **Tokens Per Second**
  - TPS measures how many tokens are delivered to the user per second after the first token. It is determined by the decode phase and reflects memory bandwidth efficiency.
- **Shared vs. Dedicated Inf.**
  - Shared inference means sending requests to a public API and paying per token. Dedicated inference means renting GPUs and running your own model server, paying per GPU-hour.
- **Inference vs. Training**
  - Training is the process of learning model weights from data. Inference is serving those weights in production to generate outputs.
- **Time to First Token**
  - TTFT measures how long it takes for a user to receive the first output token after submitting a request. It is determined primarily by the prefill phase and by queue time.
- **The Inference Stack**
  - A complete inference system has three layers: runtime, infrastructure, and tooling. The runtime layer optimizes a single model on a single instance using techniques like batching, caching, quantization, and speculation.
- **Open vs Closed Models**
  - Closed models are accessed exclusively through a vendor API; the weights are never released. Open models publish their weights for download and self-hosting.

### 1.2 Neural Networks
- **Latency vs. Throughput**
  - Lower latency means faster responses per user; higher throughput means more total requests served per unit time. These goals are often in tension.
- **Latency Percentiles**
  - Mean latency hides outliers. LLM response times follow a right-skewed distribution, so engineers measure P50, P90, P95, and P99.
- **End-to-End Metrics**
  - End-to-end latency includes inference time, network round-trip, queue time, and client-side overhead. Inference-only metrics tell you how well the model server performs; end-to-end metrics tell you what users actually experience.
- **Encoder-Decoder Arch.**
  - Neural networks can be organized as encoder-only, decoder-only, or encoder-decoder models. Modern LLMs are decoder-only.
- **Inter-Token Latency**
  - ITL is the time between successive generated tokens during decode. An ITL of 10 milliseconds corresponds to 100 tokens per second.

### 1.3 Large Language Models
- **Real-Time Factor**
  - RTF measures how quickly an ASR system can process audio relative to its duration. A system that transcribes one hour of audio in six seconds has an RTF of 600x.
- **Online vs. Offline Inf.**
  - Online inference serves real-time user-facing requests where latency matters. Offline inference processes large batches of data asynchronously where throughput and cost matter more than per-request speed.
- **Transformer Blocks**
  - Transformer blocks are the repeated hidden layers of an LLM. Each block contains an attention sublayer, a feed-forward neural network sublayer, and normalization layers.
- **Attention Mechanism**
  - Attention is the mechanism transformers use to relate each token to all previous tokens via query, key, and value projections. During decode, each new token attends to every prior token, and the KV cache stores precomputed keys and values to avoid recomputation.
- **KV Cache**
  - The KV cache stores the key and value tensors computed during attention for each previously processed token. Without it, attention would require recomputing every prior token on each decode step, making inference prohibitively slow.
- **Mixture of Experts (MoE)**
  - Mixture of Experts models replace dense linear layers with a set of smaller expert matrices, activating only a subset of experts per token via a learned router. A model like Qwen3-235B activates only 22 billion of its 235 billion parameters per forward pass, making single-user inference efficient.
- **Prefill & Decode Phases**
  - LLM inference has two distinct phases. Prefill processes the entire input sequence in parallel to build the KV cache and is compute-bound.

### 1.4 Image & Video Models
- **AI-Native Applications**
  - AI-native applications are products where generative models power the core user experience, from code editors and voice agents to customer support and media generation. Each category has different inference requirements.
- **Consumer vs. B2B**
  - Consumer applications are cost-sensitive and have unpredictable traffic spikes, requiring flexible autoscaling and low marginal cost. Business-to-business applications prioritize uptime and consistent low latency, as they often sit in the critical path of revenue-generating workflows.
- **Reasoning Models**
  - Reasoning models generate an intermediate thinking sequence before producing their final output, adding a third token sequence alongside the input and output. This reasoning trace increases total token count significantly and changes inference economics: TTFT is higher, total latency is longer, and output token costs dominate.
- **Diffusion Models**
  - Diffusion models generate images by starting from random noise and iteratively denoising it over 30 to 50 steps, guided by a text prompt. Each step runs the denoiser twice, once with conditioning and once without, to apply classifier-free guidance.
- **Image Generation Arch.**
  - Image generation models are pipelines of multiple components: a text encoder that converts the prompt into conditioning, a denoising model that iteratively refines a latent representation from noise into an image, and a variational autoencoder that converts the final latent to pixels. The denoising model is the largest and most compute-intensive component and runs up to 100 forward passes per image generation.
- **Few-Step Image Generation**
  - Few-step image generation models produce usable images in eight or fewer denoising steps by training the model to collapse the standard 30 to 50 step process into a fraction of the iterations. Techniques include latent consistency distillation and adversarial training, both of which teach the model to reach high-quality outputs in fewer passes.
- **Video Generation Models**
  - Video generation models extend image generation to three-dimensional latent space, representing width, height, and time simultaneously. They run the same number of denoising steps as image models but process far more data per step.
- **Asynchronous Inference**
  - Asynchronous inference is a fire-and-forget request model where the client submits a job, receives an immediate acknowledgment, and retrieves the result later via a webhook. It is suited for throughput-sensitive, latency-insensitive workloads like bulk document embedding or corpus transcription.

### 1.5 Bottleneck Analysis
- **Model Selection**
  - The most important decision in model performance optimization is which model to use. Smaller models with fewer parameters are faster and cheaper to serve than larger ones.
- **Model Evaluation**
  - Model evaluation, or evals, is the practice of systematically measuring model quality for a specific task or domain. Standard intelligence benchmarks like MMLU measure general capabilities but can be gamed; product-specific evals that test real use cases provide more reliable signal.
- **Fine-Tuning**
  - Fine-tuning takes a pretrained foundation model and adapts it to a specific domain by training on additional labeled data. A small fine-tuned model can match a much larger general model on constrained tasks like text-to-SQL.
- **Ops:Byte Ratio**
  - The ops:byte ratio is a property of GPU hardware that expresses the balance between compute throughput and memory bandwidth. It is calculated by dividing peak FLOPS by peak memory bandwidth, and sets the threshold that separates compute-bound from memory-bound workloads on that device.
- **Roofline Model**
  - The roofline model is a visual framework for reasoning about hardware performance limits. It plots arithmetic intensity on the x-axis against achievable performance on the y-axis, with two ceilings: a diagonal memory bandwidth ceiling for low-intensity workloads and a horizontal compute ceiling for high-intensity ones.
- **LLM Bottlenecks**
  - LLM prefill is compute-bound because it processes the entire input sequence as one large matrix multiplication, performing many operations per byte loaded. LLM decode is memory-bound because it generates tokens one at a time via vector-matrix multiplications that require loading all model weights from memory for each token while performing relatively few arithmetic operations.
- **Arithmetic Intensity**
  - Arithmetic intensity is a property of an algorithm: the number of floating-point operations performed per byte of memory read or written. A large matrix multiplication has high arithmetic intensity because the same weights participate in many operations per load; a decode forward pass has low arithmetic intensity because each weight is loaded from VRAM and used once per token.

### 1.6 Attention Optimization
- **Distillation**
  - Distillation trains a smaller student model to emulate a larger teacher model by exposing it to the teacher's probability distributions, not just its final outputs. Unlike fine-tuning on synthetic data, distillation transfers the teacher's reasoning behavior.
- **Image & Video Bottlenecks**
  - Image and video generation models are compute-bound because each denoising step applies attention over the entire latent space in parallel, similar to LLM prefill. The models are also relatively small, so memory bandwidth is not the limiting factor.
- **FlashAttention**
  - FlashAttention is a series of hand-optimized CUDA kernels that compute attention with fewer reads and writes to GPU memory by fusing the attention algorithm into a single kernel. Standard attention stores intermediate matrices to memory between steps; FlashAttention eliminates those round-trips.
- **PagedAttention**
  - PagedAttention stores the KV cache in fixed-size pages rather than a single contiguous memory block, allowing it to be distributed across GPU memory without fragmentation. It uses a lookup table to access pages on demand, reducing memory waste from over-allocation and enabling more requests to share GPU memory.
- **Attention Variants**
  - Newer attention algorithms reduce the quadratic time complexity of standard attention. Sliding window attention limits each token to attending to the nearest w tokens, turning O(N²) into O(Nw).

### 1.7 GPU Architecture
- **Compute**
  - A GPU's compute capability is determined by its Streaming Multiprocessors (SMs), each containing CUDA Cores for general arithmetic and Tensor Cores for matrix multiply-accumulate operations. Tensor Cores are the primary resource for inference, executing the matmuls that make up the majority of forward pass computation.
- **Memory**
  - GPU memory determines what fits on a single device and how fast data can move through the compute units. VRAM capacity sets the upper limit on model size and KV cache; VRAM bandwidth determines how quickly the decode phase can load weights per token.
- **Instances & Interconnects**
  - Within a node, NVLink connects GPUs one-to-one at up to 1800 GB/s on Blackwell, and NVSwitch creates an all-to-all fabric across all eight GPUs. Between nodes, InfiniBand provides inter-node connectivity at substantially lower bandwidth than NVLink.
- **Sizing & Procurement**
  - Estimating GPU requirements starts with VRAM: roughly 1 GB per billion parameters at FP8 for weights, plus at least 50 percent headroom for the KV cache. This total is rounded up to the nearest available instance size.
- **Hopper**
  - The Hopper architecture, released in 2022 with the H100 and later the H200, introduced FP8 Tensor Cores offering twice the compute throughput of FP16 and asynchronous data transfer features used by FlashAttention 3. H100 and H200 GPUs remain among the most widely deployed inference accelerators due to their maturity, broad software support, and relative availability compared to newer generations.
- **Blackwell**
  - The Blackwell architecture, released in late 2024 with the B200 and B300, added FP4 Tensor Cores and new microscaling number formats including MXFP8, MXFP4, and NVFP4. B200 GPUs offer approximately 5 petaFLOPS of FP8 compute and up to 8 TB/s of memory bandwidth.
- **Grace & Vera**
  - NVIDIA's ARM-based Grace and Vera CPUs connect to their paired GPUs via NVLink Chip-to-Chip at up to 900 GB/s, far higher than standard PCIe connections. This high-bandwidth CPU-GPU link makes offloading KV caches and LoRA weights to CPU memory practical, since data can be retrieved quickly enough to remain on the critical path.

### 1.8 GPU Models
- **NVIDIA**
  - NVIDIA GPUs are the dominant hardware for inference due to their combination of Tensor Core compute, HBM bandwidth, NVLink interconnects, and the CUDA software ecosystem. The three most relevant architectures for current inference deployments are Hopper, Blackwell, and the Grace and Vera CPU platforms that pair with them.
- **Other Accelerators**
  - Alternatives to NVIDIA GPUs include AMD MI350, Google TPUs, AWS Inferentia and Trainium, Cerebras WSE-3, and Groq LPUs. Each offers a specific advantage: AMD provides CUDA-compatible tooling via ROCm; TPUs integrate deeply with Google Cloud and JAX; Inferentia and Trainium offer cost advantages within AWS.

---

## 2. Intermediate

### 2.1 Local & Edge Inference
- **Desktop Inference**
  - Desktop inference runs on consumer hardware, primarily Apple M-series unified memory systems and high-end NVIDIA consumer GPUs. Apple hardware offers very large unified memory capacity at moderate bandwidth, enabling larger models than discrete consumer GPUs; NVIDIA consumer GPUs offer higher bandwidth with smaller capacity.
- **Mobile Inference**
  - Mobile devices run inference using vendor frameworks: Google's AI Edge SDK for Android and Apple's Foundation Models and Core ML for iOS. Hardware limitations restrict practical model sizes to one to two billion parameters on current phones.

### 2.2 CUDA
- **Writing Custom Kernels**
  - Custom kernels are written when existing libraries do not fully utilize a GPU's capabilities for a specific operation or architecture. Most production kernels are written in C++ using CUTLASS and CuTe for GEMM-style operations and FlashInfer for attention variants; Triton offers a Python-based alternative with a lower barrier to entry.
- **Kernel Selection & Fusion**
  - A CUDA kernel is a function that runs in parallel across thousands of GPU threads simultaneously. Kernel selection is choosing the best existing kernel for a specific operation; kernel fusion combines sequential kernels into one to eliminate unnecessary reads and writes to VRAM between operations.

### 2.3 Frameworks & Libraries
- **PyTorch**
  - PyTorch is the standard Python framework for building and running neural networks. It abstracts CUDA into a tensor operation API and provides automatic differentiation for training.
- **Transformers & Diffusers**
  - The transformers and diffusers libraries provide reference implementations of popular LLM and image/video generation architectures. They are not designed for production serving but are essential for understanding model configurations, downloading weights, and prototyping inference.
- **safetensors**
  - Safetensors is the standard format for storing and distributing open model weights. It uses memory mapping for fast, zero-copy loading and prevents execution of arbitrary code during deserialization, making it safer than earlier pickle-based formats.

### 2.4 Model Formats & Runtimes
- **SGLang**
  - SGLang is a high-throughput inference engine with a flexible frontend language for customizing server behavior. It has strong support for MoE models like DeepSeek and Qwen and works closely with model labs to optimize new architectural features.
- **ONNX Runtime**
  - ONNX Runtime is an open-source inference runtime that executes models exported to the ONNX format, which stores both weights and a computation graph for cross-platform portability. It supports multiple hardware backends including CUDA, DirectML, and CPU.
- **TensorRT**
  - TensorRT is NVIDIA's high-performance inference runtime that compiles PyTorch or ONNX models into optimized engines using fused kernels, quantization, and hardware-specific tuning. It is the standard choice for image and video generation models and for any workload where maximum throughput on NVIDIA hardware is the primary goal.

### 2.5 Inference Engines
- **vLLM**
  - vLLM is the most widely adopted LLM inference engine, offering broad support for model architectures, hardware platforms (NVIDIA, AMD, Google TPUs), and optimization techniques including prefix caching, quantization, speculative decoding, and parallelism. Its primary advantage is ease of adoption and the fastest day-zero support for newly released open models.
- **TensorRT-LLM**
  - TensorRT-LLM is NVIDIA's inference engine combining PyTorch-based model execution with proprietary NVIDIA kernels unavailable in other engines. It achieves the highest performance among the three major engines, with excellent support for Hopper and Blackwell architectures and NVIDIA-specific formats like NVFP4.
- **NVIDIA Dynamo**
  - Dynamo is NVIDIA's open-source distributed serving platform that sits above inference engines and provides orchestration for large-scale deployments. It adds KV-aware routing, disaggregated prefill/decode serving, multi-node parallelism, and an SLA-based planner that dynamically adjusts the number of prefill and decode workers based on TTFT and TPS targets.
- **SGLang Genai-bench**
  - SGLang Genai-bench is a benchmarking tool built into the SGLang project for measuring LLM inference throughput and latency under realistic request distributions. It supports variable input and output sequence lengths and concurrent request patterns, making it well-suited for validating SGLang and vLLM deployments before production.
- **AIPerf**
  - GenAI-Perf is NVIDIA's inference benchmarking tool, designed to work across TensorRT-LLM, Triton Inference Server, and OpenAI-compatible endpoints. It generates synthetic workloads with configurable sequence length distributions and concurrency levels and outputs standard latency and throughput metrics including TTFT, ITL, and TPS percentiles.
- **Locust**
  - Locust is a general-purpose open-source load testing framework written in Python. In inference benchmarking it is used to simulate realistic user traffic patterns — including request arrival rates, concurrency ramps, and burst scenarios — that synthetic tools do not capture.

### 2.6 Benchmarking & Profiling
- **Performance Benchmarking**
  - Benchmarking measures inference service performance under realistic workloads. Good benchmarks simulate realistic input and output sequence lengths, concurrency patterns, and request contents rather than synthetic uniform inputs.
- **Profiling Performance**
  - Profiling reveals where time is spent within a benchmark, identifying which operations consume the most compute or memory. Tools include PyTorch Profiler, NVIDIA Nsight Systems for system-wide GPU and CPU analysis, and NVIDIA Nsight Compute for per-kernel analysis.

### 2.7 Quantization
- **Post-Training Quantization**
  - Post-training quantization converts finished model weights to lower precision after training is complete, using a small calibration dataset to compute per-layer scale factors that minimize the gap between quantized and original outputs. It is the standard approach for most deployments since it requires no retraining and can be applied to any existing model.
- **Quantization-Aware Training**
  - Quantization-aware training computes scale factors and optimizes model weights jointly during training so the final model is already calibrated for the target low-precision format. This produces better quality at low precision than post-training quantization but requires retraining the model from scratch or from a checkpoint.
- **Measuring Quality Impact**
  - After quantizing a model, quality must be validated against the original. Three methods are used: perplexity scoring (lower is better, with minimal increase after quantization), standard intelligence benchmarks like MMLU or SWE-bench, and product-specific evals tailored to the actual use case.
- **ModelOpt**
  - ModelOpt is NVIDIA's toolkit for post-training quantization, supporting FP8, INT8, FP4, MXFP8, MXFP4, and NVFP4 output formats. It integrates with PyTorch and exports quantized models directly to TensorRT-LLM, vLLM, and SGLang.

### 2.8 Speculative Decoding
- **Draft-Target Decoding**
  - Draft-target speculation uses a small draft model, typically at least ten times smaller than the target, to generate draft tokens for the target model to verify. The draft model should share the same tokenizer and general behavior as the target, often being a smaller member of the same model family.
- **EAGLE**
  - EAGLE is a purpose-built speculation method where a small draft model is trained to accept hidden states from the target model as input. By seeing the target's internal representations, EAGLE achieves higher acceptance rates and longer draft sequences (up to eight tokens) than using a general-purpose small model.
- **N-gram**
  - N-gram speculation builds a dictionary during prefill that maps token prefixes to observed n-gram continuations from the input. During decode, generated tokens are looked up in this dictionary and matching suffixes become draft tokens with no separate model required.
- **Structured Outputs**
  - Structured outputs constrain model generation to a defined schema — typically JSON, a specific data type, or a function signature — so that downstream code can parse the result directly without a repair pass. Major inference engines including vLLM and SGLang ship structured output as a first-class feature.
- **Constrained Decoding**
  - Constrained decoding is the mechanism that enforces structured outputs at the token level. At each sampling step, logits for tokens that would violate the active schema or grammar are masked to zero before sampling, so only valid continuations can be selected.

### 2.9 Caching
- **Caching Approaches**
  - KV cache reuse is the primary caching strategy in LLM inference, covering both prefix caching (reusing cached KV values across requests that share a common prefix) and KV cache offloading (moving less-used cache blocks to slower storage tiers to free GPU VRAM). A related concern is cache-aware routing, which directs requests to replicas most likely to already hold the relevant cached prefix.
- **KV Cache Storage**
  - KV caches can be stored in GPU VRAM (fastest, tens to hundreds of gigabytes), CPU RAM (slower, hundreds of gigabytes to terabytes), local SSD, or networked SSD. Moving less frequently accessed KV blocks to slower storage frees VRAM for active requests.
- **Cache-Aware Routing**
  - In deployments with multiple replicas, cache-aware routing directs requests to the replica most likely to have a matching prefix already in its KV cache. Without this, a user in a long conversation may hit different replicas each turn, getting cache misses that increase latency.
- **Long Context Handling**
  - Long sequences produce KV caches large enough to strain GPU memory, slow down decode, and increase prefill time. Techniques for handling long context include FlashAttention for memory-efficient attention computation, PagedAttention for non-contiguous KV storage, chunked prefill to interleave long prefill with decode, and model-level approaches like sliding window attention that limit how many prior tokens each token attends to.

### 2.10 Model Parallelism
- **Tensor Parallelism**
  - Tensor Parallelism splits each layer's weight matrices across multiple GPUs and distributes the matmul computation. Each GPU handles a shard of each layer and the results are combined via an all-reduce operation before the next layer.
- **Expert Parallelism**
  - Expert Parallelism distributes MoE experts across GPUs so each GPU hosts multiple complete experts. Tokens are routed to the GPU holding their activated experts, and each expert runs independently within a single GPU without splitting across multiple.
- **Pipeline Parallelism**
  - Pipeline Parallelism splits an LLM's layers into sequential stages and assigns each stage to a different GPU or node. Unlike Tensor Parallelism, each GPU holds complete layers rather than layer fragments.
- **Multi-Node Inference**
  - Multi-node inference spreads a model across more than eight GPUs using InfiniBand for inter-node communication. It is necessary for the largest models where a single node lacks sufficient VRAM for weights and KV cache.

### 2.11 Disaggregation
- **NVIDIA Dynamo**
  - Dynamo supports conditional disaggregation, where requests are first sent to the decode engine and only routed to a prefill engine when the input is long or not already cached. The ratio of prefill to decode engines is configurable at runtime and can shift as traffic patterns change.

---

## 3. Advanced

### 3.1 Vision Language Models
- **Video Processing for VLMs**
  - One second of video contains 24 frames, each requiring roughly 1,000 tokens to represent at full resolution. This makes video inputs extremely long-context workloads.
- **Omni-Modal Models**
  - Omni models accept multiple input modalities and produce multiple output types in a single model. They avoid the latency of running separate specialized models in sequence but often lag behind dedicated models in quality within each modality.
- **BERT-style models**
  - BERT-style encoder-only models are the traditional architecture for text embeddings, producing a fixed-size vector by pooling the final hidden states of a bidirectional transformer. They are compact, fast, and well-suited for high-throughput indexing workloads where embedding quality is sufficient for the task.

### 3.2 Embedding Models
- **LLM-based models**
  - LLM-based embedding models use a decoder-only transformer backbone, typically between one and eight billion parameters, to produce higher-quality semantic representations than BERT-style models. They apply a pooling operation to the final layer hidden states and are trained with contrastive objectives on large-scale retrieval datasets.
- **Embedding Model Inference**
  - TensorRT-LLM with its optimized XQA attention kernel offers the best performance for embedding models with LLM backbones. FP8 quantization of weights provides performance gains with minimal quality loss, verified by checking cosine similarity between quantized and original output vectors.

### 3.3 Speech
- **Voice Activity Detection**
  - VAD is a lightweight model that monitors an audio stream or file and identifies segments containing speech, filtering out silence. It is a required preprocessing component in both real-time ASR pipelines and long-file transcription pipelines, splitting audio into discrete chunks at natural speech boundaries rather than fixed time intervals.
- **Auto. Speech Recognition**
  - ASR models like Whisper take audio input and produce text transcripts. Whisper is an encoder-decoder model where the decoder, an autoregressive transformer, dominates inference time.
- **Text-to-Speech (TTS)**
  - Modern TTS models like Orpheus TTS are fine-tuned LLMs with an expanded vocabulary that includes audio tokens. They generate audio token sequences decoded to waveforms by a small audio decoder.
- **Streaming TTS**
  - Real-time TTS streams audio continuously over WebSockets rather than returning a complete file after generation finishes. The audio decoder converts token streams to waveforms as they are generated, implemented in compiled PyTorch with dynamic batching.
- **Speech-to-Speech Models**
  - Speech-to-speech models unify ASR, reasoning, and TTS into a single model by expanding the LLM vocabulary with audio input and output tokens, eliminating the latency of cascading three separate models in sequence. Current closed models like OpenAI's gpt-4o-realtime exist but remain more expensive and less capable than well-tuned cascading pipelines of dedicated ASR, LLM, and TTS models.

### 3.4 Image & Video Generation
- **Image Generation Inference**
  - Production image generation inference uses SGLang Diffusion, TensorRT, or hand-optimized PyTorch. The most important optimization target is the attention kernel, where FlashAttention 3 or 4 outperforms the default on Hopper and Blackwell respectively.
- **Video Generation Inference**
  - Video generation models run on full nodes of eight GPUs with a batch size of one because the latent space is too large to batch effectively. Attention over the three-dimensional video latent space consumes 70 to 80 percent of compute time and is the primary optimization target.

### 3.5 Containerization
- **Dependency Management**
  - Inference dependency chains are long and fragile due to the tight coupling between CUDA versions, framework versions, and hardware architectures. Pinning exact versions of every dependency prevents unexpected breakage when upstream packages release updates.
- **NIMs**
  - NIMs are pre-built Docker containers provided by NVIDIA for popular open models, available as flexible multi-LLM containers or as GPU- and model-specific optimized containers. They provide a ready-made starting point for serving common architectures without building a custom container from scratch.

### 3.6 Autoscaling
- **Continuous Batching**
  - Continuous batching operates at the token level, swapping requests in and out of the batch as they complete individual tokens rather than waiting for a full batch to finish. This keeps GPU utilization high and minimizes the latency penalty of batching compared to static or dynamic batching.
- **Cold Starts**
  - A cold start is the time from zero replicas to serving the first request, including GPU provisioning, container image loading, model weight loading, and inference engine startup or compilation. Reducing cold start time is essential for autoscaling systems to scale down confidently and scale up responsively.
- **Routing & Load Balancing**
  - Routers make request-level decisions about which replica to send a request to, considering factors like KV cache prefix match and LoRA availability. Load balancers make system-level decisions to distribute traffic evenly across replicas.

### 3.7 Multi-Cloud
- **LoRA-Aware Routing**
  - LoRA fine-tune weights are small adapter layers loaded on top of a base model to specialize its behavior for a specific task or customer. A deployment serving many LoRA variants for the same base model must route each request to a replica that already has the required LoRA loaded in GPU memory.
- **Request Queueing**
  - A request queue holds incoming traffic when all active replicas are at capacity while autoscaling brings new replicas online. A first-in, first-out queue is the standard implementation; priority queues can give paid users better position.
- **Scale to Zero**
  - Scale to zero allows the system to run zero replicas during periods of no traffic and spin up on demand. It requires fast cold starts and robust queuing to hold incoming requests while a replica starts.
- **GPU Procurement**
  - Cloud GPUs are available from hyperscalers like AWS and GCP, GPU-focused neoclouds like CoreWeave and Nebius, and secondary markets. Procurement mechanisms include reserved instances for predictable baseline load at discounted rates, on-demand instances for flexibility, and spot instances for cost-sensitive batch workloads that tolerate preemption.
- **Capacity Management**
  - Multi-cloud inference pools GPU capacity from multiple cloud providers and regions into a single schedulable resource, treating distinct compute pools as fungible. This requires a global control plane for deployment and scaling decisions alongside per-cluster workload planes that serve traffic and report utilization.
- **Geo-Aware Load Balancing**
  - A global load balancer routes requests to the GPU cluster geographically closest to the requesting user. Network latency accumulates at roughly 5 milliseconds per time zone traversed, so routing a request from Singapore to San Francisco adds 50 to 100 milliseconds of unnecessary overhead.

### 3.8 Testing & Deployment
- **Indep. Component Scaling**
  - Multi-model pipelines, like a voice agent that runs VAD, ASR, an LLM, and TTS in sequence, have components with different hardware requirements and traffic patterns. Each component should autoscale independently based on its own load.
- **Security and Compliance**
  - Inference infrastructure must protect user inputs, model outputs, and model weights. Standard practices include data encryption, container security, network isolation, and access controls validated by third-party penetration testing.
- **Zero-Downtime Deplo.**
  - Canary deployments update inference services without interrupting live traffic by routing a small percentage of requests to the new deployment, monitoring for issues, and gradually shifting traffic over. Blue-green deployments, which cut all traffic at once to a parallel environment, are impractical for large inference workloads because they require doubling GPU capacity during the transition.
- **Cost Estimation**
  - Dedicated inference cost depends on batch sizing, traffic patterns, and sequence lengths rather than simply on token count. Comparing dedicated versus API costs requires converting per-token API pricing into total cost over a representative time window and comparing it to GPU-hour costs at the same traffic volume.
- **Observability**
  - Inference observability tracks total request volume, input and output sequence lengths, response codes, latency percentiles (P50, P90, P99 of TTFT, TPS, and end-to-end latency), replica count, GPU utilization, and queue depth. These metrics are interdependent; a latency spike could come from long input sequences, high concurrency, or a hardware issue.

---

## 4. Optional / Specialized Topics

- The Inference Stack
- Open vs Closed Models
- Inter-Token Latency
- KV Cache
- Mixture of Experts (MoE)
- Prefill & Decode Phases
- Image Generation Arch.
- Few-Step Image Generation
- Video Generation Models
- Asynchronous Inference
- Roofline Model
- LLM Bottlenecks
- Arithmetic Intensity
- Attention Variants
- Hopper
- Blackwell
- Grace & Vera
- AIPerf
- Locust
- Constrained Decoding
- Speech-to-Speech Models
- Capacity Management
- Geo-Aware Load Balancing
- Observability

---

## 5. References

- [Inference Engineering Specialist Roadmap](https://roadmap.sh/inference-engineering)

---

## 6. Related Roles / Topics

### Related Roles
- AI Engineer
- Backend Developer
- MLOps Engineer
- DevOps Engineer

### Related Skills
- Prompt Engineering
- C++
- Docker
- Kubernetes