import string, random

while True :
    lenght = int(input('Enter A Preferred Password Lenght : '))

    # you can edit the lenght message in input.
    # remember you can only put number for answer in lenght!
    
    chars = string.ascii_letters + string.digits + '@!#$%*&+-'

    # you can edit the '@!#$%*&+-' in chars or change string.

    password = ''.join([random.choice(chars) for i in range(lenght)])

    print('Your Password : {}'.format(password))

    # you can edit message in print and do not touch format!

    while True :

        answer = input('Do You Want Another Password (Y/N) : ').lower()

        # you can edit message in input do not touch lower!

        if answer == 'n' or answer == 'y' :
            break

    if answer == 'n' :
       break