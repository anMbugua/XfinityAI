from xfinity_ai.chat.conversation import Conversation


chat = Conversation()

chat.add_user_message(
    "Hello XfinityAI"
)

chat.add_assistant_message(
    "System online"
)


print(chat.history())
