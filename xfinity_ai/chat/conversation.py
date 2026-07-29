from xfinity_ai.chat.message import Message


class Conversation:

    def __init__(self, session_id=None):

        self.session_id = session_id
        self.messages = []


    def add_message(self, role, content):

        message = Message(
            role=role,
            content=content
        )

        self.messages.append(message)


    def add_user_message(self, content):

        self.add_message(
            "user",
            content
        )


    def add_assistant_message(self, content):

        self.add_message(
            "assistant",
            content
        )


    def history(self):

        return [
            message.to_dict()
            for message in self.messages
        ]


    def clear(self):

        self.messages.clear()


    def context(self):

        return "\n".join(
            [
                f"{m.role}: {m.content}"
                for m in self.messages
            ]
        )
