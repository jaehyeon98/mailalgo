data = input()

data = data.replace('XXXX', 'AAAA')
data = data.replace('XX', 'BB')
if 'X' in data:
    print(-1)
else:
    print(data)