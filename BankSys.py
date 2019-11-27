print('欢迎来到方氏银行系统')
# 主菜单内容
main_menu={1:'注册',2:'登录',3:'查询所有用户',4:'修改用户',5:'删除用户',6:'退出'}#menuid=1
# 用户菜单内容
menu={1:'查询余额',2:'存款',3:'取款',4:'修改密码',5:'退出登录'}#menuid=2

# 显示菜单函数，menuID=1为主菜单，menuID=2为用户菜单
def ShowMenu(menuID):
    if menuID==1:
        print('=========================系统菜单=========================')
        for e in main_menu.keys():
            print(str(e)+'.'+main_menu[e],end=' ')
        print('\n==========================================================')
    elif menuID==2:
        print('=========================用户菜单=========================')
        for e in menu.keys():
            print(str(e)+'.'+menu[e],end=' ')
        print('\n==========================================================')
# 存钱、取钱函数
# op值为save是存，op值为deliver是取
# num是交易金额
def Money(op,num):
    if op=='save':
        now_money=users[cardid]['money']
        fina_money=num+now_money
        users[cardid]['money']=fina_money
        print('存款成功！')
        print('当前账户余额为：'+str(users[cardid]['money'])+'\n')
    elif op=='deliver':
        now_money=users[cardid]['money']
        fina_money=now_money-num
        # 判断余额是否支持取款金额
        if fina_money<0:
            print('余额不足，取款失败！')
        else:
            users[cardid]['money']=fina_money
            print('取款成功！')
            print('当前账户余额为：'+str(users[cardid]['money'])+'\n')
       
ShowMenu(1)
# 定义用户字典，初始为空
users={}

# 系统功能部分
while True:
    # optipon 为系统功能选项
    option=input('请选择功能序号：')
    option=int(option)
    # 注册账户
    if option == 1:
        # 卡号
        cardid=input('请输入卡号：')
        # 姓名
        name=input('请输入姓名：')
        # 密码
        pwd=input('请输入密码：')
        # 判断卡号是否存在，保证卡号唯一
        for e in users.keys():
            if e==cardid:
                print('此卡号已存在，请重新输入卡号！')
                cardid=input('请输入：')
                break
            else:
                pass
        users[cardid]={'name':name,'pwd':pwd,'money':0}
        print('账户初始化成功！')
        print('卡号：'+cardid)
        print('用户名：'+users[cardid]['name'])
        print('余额：'+str(users[cardid]['money']))
        ShowMenu(1)
    # 用户登录
    if option==2:
        cardid=input('请输入卡号：')
        pwd=input('请输入密码：')
        if cardid in users:
            if users[cardid]['pwd']==pwd:
                print('登录成功！\n')
                ShowMenu(2)
                # 进入用户系统
                while True:
                    option=input('请选择功能序号：')
                    option=int(option)
                    # 查询余额
                    if option==1:
                        print('您当前余额为：'+str(users[cardid]['money'])+'元\n')
                        ShowMenu(2)
                    # 存款
                    if option==2:
                        money_in=input('请输入存款金额：')
                        money_in=int(money_in)
                        Money('save',money_in)
                        ShowMenu(2)
                    # 取款
                    if option==3:
                        money_out=input('请输入取款金额：')
                        money_out=int(money_out)
                        Money('deliver',money_out)
                        ShowMenu(2)
                    # 修改密码
                    if option==4:
                        old_pwd=input('请输入原来的密码以确认身份：')
                        if old_pwd==users[cardid]['pwd']:
                            new_pwd=input('身份验证通过，请输入新密码：')
                            users[cardid]['pwd']=new_pwd
                            print('密码修改成功！\n')
                        else:
                            print('身份验证不通过，请重试！')
                        ShowMenu(2)
                    if option==5:
                        break
            else:
                print('登录失败：账号或密码错误！')
        else:
            print('登录失败：此卡号未注册！')
        ShowMenu(1)
    # 查询所有用户
    if option==3:
        print('卡号    用户名    密码    余额')
        for e in users:
            print(e+'     '+users[e]['name']+'      '+users[e]['pwd']+'      '+str(users[e]['money']))
            print('-----------------------------')
        ShowMenu(1)
    # 修改信息
    if option==4:
        fina=''
        alert_id=input('请输入要修改的信息的卡号：')
        for e in users.keys():
            if e==alert_id:
                fina='ok'
        if fina=='ok':
            new_name=input('请输入新用户名：')
            users[alert_id]['name']=new_name
            print('修改成功!\n')
        else:
            print('修改失败！账户不存在！\n')

        ShowMenu(1)
    # 删除账户
    if option==5:
        delete_id=input('请输入要删除的卡号：')
        res=' '
        for e in users.keys():
            if e==delete_id: 
                res='found'                  
        if res=='found':
            del users[delete_id]
            print('删除成功！\n')
        else:
            print('账户不存在，删除失败！\n')  
        ShowMenu(1)
    # 退出
    if option==6:
        print('再见！')
        break