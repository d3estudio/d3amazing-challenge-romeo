class test:
    def __init__(self):
        self.user = []


    def add(self, name):
        self.user.append({ 
            'user_id': name,
            'chat_status': 1 
            })


    def get_status(self, id):

        for x in self.user:
            if x['user_id'] == id:
                status =  x['chat_status']
                x['chat_status'] += 1
                return status

    def chamou(self, str):

        print(str)

    def falar(self, id):
        num = 10
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:"chamou opsção 3",
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
        return switcher.get(num, "complex")

teste = test()

teste.add("novo")

# for x in teste.user: print(x["chat_status"])

teste.get_status("novo")

str = teste.falar("novo")

print(str)

# for x in teste.user: print(x["chat_status"])
