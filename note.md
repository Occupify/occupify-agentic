---
Agents don't read this file, skip
---

Workspace: /home/phandinhminh/Downloads/Occupify/occupify-agentic/
Output: md file

Hi lead, I need you to talk and discuss with me first, then create a plan later

Please read in the /home/phandinhminh/Downloads/Occupify/occupify-agentic/docs/usecases.md

You will see bunch of use cases

I need to setup first:
- I just need the lightweight python app for the AI agent service - Also tell me how to organize the folder structure in the app
- You brainstrom with me on how should we design the application based on the use cases, what database should we use also
- For the tool call, this is simply call to other services with rabbit mq (please scan example in /home/phandinhminh/Downloads/Occupify/occupify-core/src/main/java/com/occupify/core/config/RabbitMQConfig.java)
- I do need the log from the agent flow (this should be easy by you just need the helper log function)
- The AI that we using in this app is GLM, I have put api_key in the .env
- To save tokens, and utilize the powerful websearch from Gemini, you can send the message to gemini ai squad to help you more on research
- I need to setup the Dockerfile (containerize my python application) and docker-compose (where you pull the necessary library)
- I need to setup the CI pipeline (no need CD at this stage) to run the test cases