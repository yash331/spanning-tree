import bridge
import os
trace=int(input())
n=int(input())
bridges=[]
la={}

for a1 in range(65,91):
    y=bridge.Lan(chr(a1))
    la[chr(a1)]=y

for a1 in range(n):
    s=input().split(':')
    l=s[1][1:].split()
    lta=[]

    for a2 in l:
        lta.append(la[a2])


    b=bridge.Bridge(s[0],lta)
    bridges.append(b)

try:
    os.remove('trace.txt')
except:
    pass



if True:
    f=open('trace.txt','x')
    time=0


    while True:
        for a1 in bridges:
            for a2 in a1.lan:
                for a9 in a2.message:
                    if (a1.name!=a9[0]):
                        f.write(str(time))
                        f.write(' r ')
                        f.write(a1.name)
                        f.write(' ')
                        f.write(a2.name)
                        f.write(' ')
                        f.write(a9[0])
                        f.write(',')
                        f.write(str(a9[1]))
                        f.write(',')
                        f.write(a9[2])
                        f.write('\n')                    

        f.write('\n')

        for a3 in bridges:
            a3.determine_sending_message()

        for a5 in bridges:
            for a6 in a5.lan:
                a6.clear_message()

        for a7 in bridges:
            a7.sending_message()

        for a4 in bridges:
            for a8 in a4.lan:
                for a10 in a8.message:
                    if(a10[0]==a4.name):
                        f.write(str(time))
                        f.write(' s ')
                        f.write(a4.name)
                        f.write(' ')
                        f.write(a8.name)
                        f.write(' ')
                        f.write(a10[0])
                        f.write(',')
                        f.write(str(a10[1]))
                        f.write(',')
                        f.write(a10[2])                    
                        f.write('\n')


        f.write('\n')

        time+=1
        breaking=True
        first_root_bridge=bridges[0].lan[0].message[0][2]

        for a11 in bridges:
            for a12 in a11.lan:
                for a13 in a12.message:
                    if(a13[2]!=first_root_bridge):
                        breaking=False

        

        if breaking:
            break

    f.close()

    for a14 in bridges:
        print(a14.name,end='')
        print(':',end=' ')
        names=[]
        for a15 in a14.lan:
            names.append(a15.name)

        names.sort()

        for a16 in names:
            print(a16,end='')
            print('-',end='')
            print(a14.port[a16][1],end=' ')

        print()

if trace==0:
    os.remove('trace.txt')








                


