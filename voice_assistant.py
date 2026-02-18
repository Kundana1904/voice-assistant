import os
from dotenv import load_dotenv
load_dotenv()
AGENT_ID=os.getenv("AGENT_ID")
API_KEY=os.getenv("API_KEY")
print("API_KEY =", API_KEY)
print("AGENT_ID =", AGENT_ID)

def print_agent_response(response):
    print(f"Agent:{response}")
def print_interrupted_response(original,corrected):
    print(f"Agent interrupted,truncated response:{corrected}")
def print_user_transcript(transcript):
    print(f"User:{transcript}")
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.conversational_ai.conversation_config import ConversationConfig

prompt="You are a friendly assistant."
first_message="Hello! How can I help you today?"
conversation_override={
    "agent":{
        "prompt":{
            "prompt":prompt,
        },
        "first_message":first_message,
    },
}
config=ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
)
client=ElevenLabs(api_key=API_KEY)
conversation=Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)
conversation.start_session()
