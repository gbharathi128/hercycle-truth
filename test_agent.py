import vertexai
from vertexai.agent_engines import AgentEngine

vertexai.init(project="your-project-id", location="us-central1")

# Get deployed agent
agents_list = list(AgentEngine.list())
if agents_list:
    remote_agent = agents_list[0]
    async for item in remote_agent.async_stream_query(
        message="What's a good PCOS diet for Monday?",
        user_id="test_user"
    ):
        print(item)
else:
    print("Deploy first!")
