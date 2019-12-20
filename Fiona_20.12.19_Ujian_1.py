#No 1

def Hashtag(string):
    if len(string) == 0:
        print(False)
    else:
        words = string.split()
        new = []
        for i in words:
            temp = []
            temp = i.capitalize()
            new.append(temp)
        final = ''
        for j in new:
            final += j
        if len(final) > 140 or len(final) == 0:
            print(False)
        else:
            hashtag = '"'+ '#' + final + '"'
            print(hashtag)
        
# Hashtag(" Hello there how are you doing")
# Hashtag("  Hello World  ")
# Hashtag("  fiona leo la la la la  ")
# Hashtag("   ")
# Hashtag("")



#No 2

def create_phone_number(number):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    able = True
    if len(number) != 10:
        able = False
    else:
        phone = ''
        for i in range(len(number)):
            if number[i] in numbers:
                if i == 0:
                    phone += '"'
                    phone += '('
                    phone += str(number[i])
                elif i == 2:
                    phone += str(number[i])
                    phone += ') '
                elif i == 5:
                    phone += str(number[i])
                    phone += '-'
                elif i == len(number)-1:
                    phone += str(number[i])
                    phone += '"'
                else:
                    phone += str(number[i])
            else:
                able = False
                break
    if able == True:
        print(phone)
    else:
        print('Invalid Input')

# create_phone_number([1,2,3,4,5,6,7,8,9,0])
# create_phone_number([0,2,1,5,8,9,0,1,0,6])
# create_phone_number([0,2,1,5,8,9,0,1,0,6,8])
# create_phone_number([0,2,1,'z',8,9,0,1,0,6])



#No 3

def sort_odd_even(num):
    odd = []
    even = []
    final = []
    even_only = []
    odd_only = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
            even.sort(reverse = True)
        else:
            odd.append(i)
            odd.sort()
    for j in range(len(num)):
        if num[j]%2 == 0:
            final.append(even[0])
            even_only.append(even[0])
            odd_only.append(' ')
            even.pop(0)
        else:
            final.append(odd[0])
            odd_only.append(odd[0])
            even_only.append(' ')
            odd.pop(0)
    index_even = ''
    index_odd = ''
    for k in range(len(even_only)):
        if even_only[k] != ' ':
            index_even += str(k) + ' '
    for l in range(len(odd_only)):
        if odd_only[l] != ' ':
            index_odd += str(l) + ' '
    print(final)
    if len(num) != 0:
        print('\n')
        print('Odds numbers ascending: {} in the index {}'.format(odd_only, index_odd))
        print('Evens numbers descending: {} in the index {}'.format(even_only, index_even))

# sort_odd_even([5,3,2,8,1,4])
# sort_odd_even([8,7,1,0,3,2])
# sort_odd_even([8,7,1,0,3,2,7,6,5,4,3])
# sort_odd_even([])



#No 4

def hollow_triangle(size):
    z = ''
    for i in range(size):
        for j in range(size*2-1):
            if i == size-1:
                z += '#'
            else:
                if j == size-1-i or j == size-1+i:
                    z += '#'
                else:
                    z += '_'
            
        z += '\n'
    print(z)

# hollow_triangle(0)
# hollow_triangle(1)
# hollow_triangle(2)
# hollow_triangle(3)
# hollow_triangle(4)
# hollow_triangle(5)
# hollow_triangle(6)
# hollow_triangle(7)
# hollow_triangle(8)