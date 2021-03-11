from interactive_romeo import user
import random

class conversation_romeo:

    def __init__(self):
        self.user = user.User_chat()

    def answer(self, user_id, text):

        if self.user.is_in(user_id):
            num = self.user.get_status(user_id, text)
            basic_answer = self.basic_answer(num)
            if basic_answer == "complex":
                return self.complex_anser(num)
            else:
                return basic_answer
        else:
            return "mensagem de ola"
        
    def hi_message(self):
        
        n = random.randint(0,3)
        switcher={
            0:'mensagem de ola',
            1:'mensagem de ola',
            2:'mensagem de ola',
            3:'mensagem de ola',
        }
        return switcher.get(n)

    def basic_answer(self, num):
        switcher={
            1:'explicar oq ele faz',
            2:'Tuesday',
            3:'Wednesday',
            4:'Thursday',
            5:'Friday',
            6:'Saturday'
        }
        return switcher.get(num,"complex")

    def complex_anser(self, num):
        switcher={
            1:'Monday',
            2:'Tuesday',
            3:'Wednesday',
            4:'Thursday',
            5:'Friday',
            6:'Saturday'
        }
        return switcher.get(num,"complex")


        