import re
class User_chat:
    def __init__(self):
        self.users = []

    def is_in(self, id: str):

        if self.is_new_user(id):
            self.add(id)
            return False
        else:
            return True

    def is_new_user(self, id: str):

        for x in self.users:
            if x['user_id'] == id:
                return False
        return True
        
    def add(self, id: str):

        self.users.append({ 
            'user_id': id,
            'chat_status': 1,
            'recipient': ""
            })

    def get_status(self, id: str, text: str):
        key = -1
        for user in self.users:
            key += 1
            if user['user_id'] == id:
                status =  user['chat_status']

                if status == 1:
                    user['chat_status'] += 1
                    return status

                if text.lower() == "voltar":
                    user['chat_status'] == 0
                    return status

                elif [2,3].__contains__(status):

                    n =  self.user_imput(text.lower(), status)

                    if [2,3].__contains__(n):
                        user['chat_status'] += 1
                        return status

                    elif n == 4:
                        self.users.pop(key)
                        return n

                    elif n == 5:
                        user['chat_status'] = 5
                        return n

                    elif n == 8:
                        user['chat_status'] = 8
                        return n

                elif [5,6,7,8,9,10].__contains__(status):

                    recipient_id = self.whom_to_send(text)
                    print("qual foi : " + recipient_id)

                    if recipient_id != "none":
                        if [5,6,7].__contains__(status):
                            user['chat_status'] = 13
                            user['recipient'] = recipient_id
                            return 11

                        if [8,9,10].__contains__(status):
                            user['chat_status'] = 14
                            user['recipient'] = recipient_id
                            return 12

                    elif [5,6,8,9].__contains__(status):
                        user['chat_status'] += 1
                        return user['chat_status']

                    elif [7,10].__contains__(status):
                        self.users.pop(key)
                        return 4

                elif 13 == status:

                    return[status,user['recipient'],text]

                elif 14 == status:
                    
                    return[status,user['recipient'],text]

    def user_imput(self, text: str, id: int):
        if text == "correio":
            return 5
        if text == "ajuda":
            return 8
        else:
            return id

    def whom_to_send(self, text: str):

        if text[0] == '<' and text[1] == '@' and text[len(text) - 1] == '>':
            recipient_id = text[2:len(text)-1]
            if re.match('^[A-Z0-9_.-]*$', recipient_id):
                return recipient_id
        return "none"
            
    # def elegant_mail(self, text: str):

    #     return ""

    # def ready_mail(self, text: str):
    
    #     return ""