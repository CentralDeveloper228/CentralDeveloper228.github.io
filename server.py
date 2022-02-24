f = open('token.txt', mode='w')
f.write('token: 'f'{token}' '\n')
f.write('data: ' 'none')
f.close()
return f"{token}"