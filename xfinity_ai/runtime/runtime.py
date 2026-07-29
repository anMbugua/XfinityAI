from xfinity_ai.chat.conversation import Conversation


class Runtime:


    def __init__(self):

        self.conversation = Conversation()


    def receive(self, message):

        self.conversation.add_user_message(
            message
        )


    def respond(self, response):

        self.conversation.add_assistant_message(
            response
        )


    def history(self):

        return self.conversation.history()
