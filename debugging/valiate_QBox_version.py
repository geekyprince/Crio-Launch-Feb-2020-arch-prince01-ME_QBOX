a=input()
d=input()
z="/home/crio-user/workspace/arch-prince01-ME_QBOX/debugging/"
b=open(z+d, 'r')


k = open(z+'high_memory_usage_versions','r')
s=""
fl = 1
for i in k:
    s = i
    if(s == a):
        print('failure: Version '+ s + ' fails memory usage')
        fl = 0
if(fl == 1):
    print('success')

k=open(z+'high_cpu_usage_versions','r')
s=""
f1 = 1
for i in k:
    s=i
    if(s==a):
        print('failure: Version '+ s + ' fails cpu usage')
        fl = 0
if(fl == 1):
    print('success')


k=open(z+'incorrect_file_permission_versions','r')
s=""
f1 = 1
for i in k:
    s=i
    if(s==a):
        print('failure: Version '+ s + ' fails file permission')
        fl = 0
if(fl == 1):
    print('success')

k=open(z+'increased_time_taken_versions','r')
s=""
f1 = 1
for i in k:
    s=i
    if(s==a):
        print('failure: Version '+ s + ' fails time taken')
        fl = 0
if(fl == 1):
    print('success')

k=open(z+'file_transfer_not_possible_versions','r')
s=""
f1 = 1
for i in k:
    s=i
    if(s==a):
        print('failure: Version '+ s + ' file transfer not possible in download')
        fl = 0
if(fl == 1):
    print('success')