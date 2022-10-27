x = str(input('Digite uma letra: ')).lower().strip()[0]

if x not in 'aeiou':
    print(f'"{x}" é consoante!')
else:
    print(f'"{x}" é vogal!')