import os
import autogen
from autogen import AssistantAgent, UserProxyAgent
from messages import system_message_airline_agent, system_message_crew_agent, system_message_Food_Agent, system_message_HR_Management_Agent

os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_ENDPOINT"] = ""

config_list = [
    {
        "model": "gpt-4",
        "api_key": "",
        "base_url": "",
        "api_type": "azure",
        "api_version": "2024-02-15-preview"
    }
]

llm_config = {
    "seed": 42, 
    "temperature": 0,
    "config_list": config_list,
}

A_agent = AssistantAgent(
        name="A", llm_config=llm_config,
        system_message= system_message_A
    )
B_agent = AssistantAgent(
        name="B", llm_config=llm_config,
        system_message= system_message_B
         
    )

C_agent = AssistantAgent(
        name="C", llm_config=llm_config,
        system_message= system_message_C
         
    )

D_agent = AssistantAgent(
        name="D", llm_config=llm_config,
        system_message= system_message_D
         
    )
user_proxy = UserProxyAgent(
        name="User_Proxy",
        human_input_mode="NEVER",
        llm_config=llm_config,
        max_consecutive_auto_reply=20,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config=False,
    )

groupchat = autogen.GroupChat(agents=[A, B, C, D, user_proxy], messages=[],speaker_selection_method="round_robin", max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

res = user_proxy.initiate_chat(manager, message="""""")