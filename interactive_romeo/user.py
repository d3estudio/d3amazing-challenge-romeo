class User_chat:
    def __init__(self):
        self.user = []

    def is_in(self, id):
        
        if self.is_new_user(id):
            self.add(id)
            return False
        else:
            return True
        
    def add(self, id):

        self.user.append({ 
            'user_id': id,
            'chat_status': 1 
            })

    def is_new_user(self, id):

        for x in self.user:
            if x['user_id'] == id:
                return False
        return True
        

    def get_status(self, id):

        for x in self.user:
            if x['user_id'] == id:
                status =  x['chat_status']
                x['chat_status'] += 1
                return status

    def set_status(self, id , num):

        for x in self.user:
            if x['user_id'] == id:
                x['chat_status'] = num
    
    