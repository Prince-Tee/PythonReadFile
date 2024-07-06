file = open('file.txt','r')

f= file.read()
print(f)

split1 = f.split('\n')
print(split1)
       

for each in split1:
   split2 = each.split(' ')
   print(split2)
   total = int(split2[1])+ int(split2[2]) + int(split2[3]) + int(split2[4])
   print(total)
   avg = (total/4)
   print(avg)
   if avg < 50 :
       print('you failed')
   else:
       print('you passed')
