def print_info(name,age,sex):
    print('姓名:'+name)
    print('年龄:'+str(age))
    print('性别:'+sex)

print_info('吴正凯',20,'男') 


d = 1,2,3
a,b,c=d
print(a,b,c)


def pirnt_full_name(first_name,middle_name,last_name):
    if middle_name:
        full_name=first_name+middle_name+last_name
        print(full_name.title())
    else:
        full_name=first_name+''+last_name
    return full_name

fullname=pirnt_full_name('li','chun','shan')
print(fullname)

fullname=pirnt_full_name('li','','shan')
print(fullname)

