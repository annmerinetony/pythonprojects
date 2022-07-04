# def vaccination(func):
#     def data(a,b):
#         if b<18:
#             raise Exception('unable to vaccinated')
#         else:
#             return func(a,b)
#     return data
# @vaccination
# def vaccine(name,age):
#     return'vaccinated successfully'
# print(vaccine('ann',10))
# def valid(func):
#     def number(n):
#         if n=='+911294567890':
#             print('valid')
#             return func(n)
#         else:
#             raise Exception('not valid')
#     return number
# @valid
# def changenumber(phnnum):
#     newnum=phnnum
#     return newnum
# print(changenumber('+911294567894'))
def mail(func):
    def mail_check(a,b):
        if a=='abcd@gmail.com':
            return func(a,b)
        else:
            print('invalid mail id')
    return mail_check
@mail
def login(mailid,psw):
    return 'successfully completed login process'
print(login('abcd@gmail.com',5456))

