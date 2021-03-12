
# class test:
#     def __init__(self):
#         self.user = []


#     def add(self, name: str):
#         self.user.append({ 
#             'user_id': name,
#             'chat_status': 1 
#             })


#     def get_status(self, id):

#         for x in self.user:
#             if x['user_id'] == id:
#                 status =  x['chat_status']
#                 x['chat_status'] += 1
#                 return status

#     def chamou(self, str):

#         print(str)

#     def falar(self, id):
#         num = 'Tuesday'
#         switcher={
#                 'Sunday': 1,
#                 'Monday': 1,
#                 'Tuesday': 5,
#                 'Thursday': 1,
#                 'Friday': 1
#              }
#         return switcher.get(num, "complex")

#     def oq(self):
#         return ["oauhjsf","asdasdasdasdasd"]

# teste = test()

# teste.add(1)

# print(teste.user)

# teste.add("novo")
# teste.add("velho")
# teste.add("atual")

# # for x in teste.user: print(x["chat_status"])

# teste.user.pop(1)

# print(teste.user)

# frases = teste.oq()

# if frases.__class__() == []:
#     print(frases[0])
#     print(frases[1])
# elif frases.__class__() == "":
#     print(frases)

# var = ["oqdoknqowc",11]

# switcher={
#             0:'explicar oq ele faz',
#             1:'falar que nao entendeu',
#             2:'falar que nao entendeu de novo',
#             3:'desistir',
#             4:'mandar correio elegante, para quem?',
#             5:'mandar mensagem pronta, para quem?',
#             6:'nao entendi pra quem mandar',
#             7:'nao entendi pra quem mandar',
#             8:'qual a mensagem?',
#             9:'qual o tipo de mensagem pronta?',
#             10:'asdasdas'
#         }
# print(switcher.get(var,"complex"))

text = "test"

praises = open(text +'.txt','r')
ok = praises.read().split("\n")

print(ok[0])