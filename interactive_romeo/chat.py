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
            return self.hi_messages()
        
    def hi_messages(self):

        messages = open('./interactive_romeo/sentences/hi_messages.txt','r')
        message = messages.read().split("\n")
        n = random.randint(0,len(message) - 1)
        return message[n]

    def basic_answer(self, num):

        print("num: " + str(num))
        print("type: " + str(type(num)))
        
        messages = open('./interactive_romeo/sentences/basic_answer.txt','r')
        message = messages.read().split("\n")
        return message[num]

    def complex_anser(self, num, text):
 
        messages = open('./interactive_romeo/sentences/complex_anser.txt','r')
        message = messages.read().split("\n")
        
        if num[0] == 14:

            answer = message[0]
            send =  message[2] + '\n\n"' + text + '"\n\n' + message[4]

        if num[0] == 15:

            answer = message[1]
            praises = open('./interactive_romeo/sentences/ready_' + '\n\n"' + text + '"\n\n' +'.txt','r')
            praise = praises.read().split("\n")
            n = random.randint(0,len(praise) - 1)
            send =   message[3] + praise[n] + message[4]

        return[answer,num[1],send]