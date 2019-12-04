import random

def luck_times(times):
    index = 0
    first_num,second_num,third_num= 0,0,0
    while True:
        if index<times:
            index +=1
            luck_num = random.random()
            if luck_num>=0 and luck_num<0.05:
                first_num +=1
            elif luck_num>=0.05 and luck_num<0.4:
                second_num +=1
            else:
                third_num +=1               
        else:
            print(
                '一等奖人数为：'+str(first_num)+
                '\n二等奖人数为：'+str(second_num)+
                '\n三等奖人数为：'+str(third_num)
                )
            break

luck_times(1000)