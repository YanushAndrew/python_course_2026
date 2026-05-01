while 1:
    user_mail = input('enter some mail, please: ')
    
    if(user_mail.find('@')== -1):
        print('You should print email: <your-address>@<domain.domain>')
        continue
    if(user_mail.count('@') > 1):
        print('To much "@" in your mail.')
        continue

    updated_user_mail = user_mail[0]
    updated_user_mail += ('*' * (user_mail.find('@')-2))
    updated_user_mail += user_mail[(user_mail.find('@')-1):-1]
    updated_user_mail += user_mail[-1]
    print(updated_user_mail)
    print(user_mail)
    break
