# negyedik alkalom

def osszeadas(a,b):
    return a + b

# Főprogram

if __name__ == '__main__':
    x = 4
    y = 6
    print(osszeadas(x,y))

sorozat = [1, 5, 9, 6, 8, 7]
for elem in sorozat:
    if elem == 5:
        continue
    print(elem)
    if elem == 6:
        break
else:
    print('vége')

for elem in range(1, 6, 2):
    print(elem)

for elem in "\tJó reggelt!":
    print(elem)

# hibás futás

s = 0
x = 'ötven'
try:
    eredmeny = x / s
except Exception as e:
    print(e)
    print('\tHiba - nullával való osztás!')
except ValueError:
    eredmeny = 1
    print('egyik érték hibás')
else:
    print(eredmeny)
finally:
    print('program vége')

