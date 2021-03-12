from interactive_romeo import user
import random

class conversation_romeo:

    def __init__(self):
        self.user = user.User_chat()

    def answer(self, user_id: str, text: str):

        if self.user.is_in(user_id):

            num = self.user.get_status(user_id, text)

            if num.__class__() != []:
                return self.basic_answer(num)
            else:
                return self.complex_anser(num, text)
        else:
            return self.hi_message()
        
    def hi_message(self):
        
        n = random.randint(0,3)
        switcher={
            0:'mensagem de ola 1',
            1:'mensagem de ola 2',
            2:'mensagem de ola 3',
            3:'mensagem de ola 4',
        }
        return switcher.get(n)

    def basic_answer(self, num):
        switcher={
            0:'explicar oq ele faz pela segunda vez',
            1:'explicar oq ele faz',
            2:'falar que nao entendeu',
            3:'falar que nao entendeu de novo',
            4:'desistir',
            5:'mandar correio elegante, para quem?',
            6:'nao entendi pra quem mandar o correio',
            7:'nao entendi pra quem mandar o correio vou desistir',
            8:'mandar mensagem pronta, para quem?',
            9:'nao entendi pra quem mandar a mensagem?',
            10:'nao entendi pra quem mandar a mensagem vou desistir?',
            11:'qual a mensagem?',
            12:'qual o tipo de mensagem pronta?'
        }
        return switcher.get(num,"complex")

    def complex_anser(self, num, text):
        switcher={
            13:'falar que mandou a mensagem',
            14:'mostrar que mandou a mensagem pronta',
        }
        answer = switcher.get(num[0],"complex")
        return[answer,num[1],text]

        