print("################################")
def echo(n):
    for _ in range(n):
        received = yield
        print(f'recevied: {received}')

e = echo(3)  # generator status: CREATED
next(e)  # generator status: SUSPENDED / Prime first before sending data
e.send('la')  # Resumed
e.send('lala')  # Resumed
# e.send('lalala')  # CLOSED


print("################################")
def echo2(n):
    for i in range(n):
        received = yield i ** 2
        print(f'received: {received}')

e2 = echo2(3)
next(e2)  # Prime
e2.send('ka')
e2.send('kaka')
e2.send('kakaka')



