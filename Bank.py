# 账号类
class Acount():
    def __init__(self,id,name,pwd,money):
        self.name=name
        self.id=id
        self.pwd=pwd
        self.money=money
    # 存钱
    def Save(self,money):
        self.money += money
    # 取钱
    def Draw(self,money):
        self.money -= money
    #  查询余额   
    def Qurey(self):
        return self.money
    # 修改密码
    def AlterPwd(self,newPwd):
        self.pwd=newPwd
        print("修改成功")
      
# 银行类
class Bank():

    def __init__(self):
        self.account=[]
    # 查询所有账户
    def ShowAccount(self):
        for i in self.account:
            print('用户id：'+str(i.id)+' 用户名：'+i.name+' 账户余额：'+str(i.money))
    # 修改账户信息
    def AlterInfo(self):
        id = int(input('请输入要修改的账户id：'))
        if self.account[id] in self.account:
            newName = input('请输入新用户名：')
            self.account[id].name = newName
            print('信息修改成功！')
            self.ShowAccount()
        else:
            print('账户不存在！')  
    # 删除用户
    def DropAccount(self):
        id = int(input('请输入要删除的账户id：'))
        if self.account[id] in self.account:
            del self.account[id]
        else:
            print('账户不存在！')
    # 注册
    def Logon(self,account):
        self.account.append(account)
        print('注册成功！')
    # 退出登录
    def Logout(self):
        print('欢迎下次光临！')
        exit(0)
    # 登录
    def login(self):
        accountId = int(input('请输入账户id：'))
        pwd = input('请输入账户密码：')
        if self.account[accountId].pwd == pwd:
            print('登录成功！')
            while True:
                print('=========================系统菜单=========================')
                print('1.查询所有用户  2.修改用户  3.删除用户  4.退出登录')
                choice = int(input('请输入功能选项：'))
                if choice == 1:
                    self.ShowAccount()
                if choice == 2:
                    self.AlterInfo()
                if choice == 3:
                    self.DropAccount()
                if choice == 4:
                    self.Logout()
        else:
            print('账号或密码错误')
# 创建账户对象
a = Acount(0,'fx','pwd',0)
print(a.Qurey())
# 创建银行对象
bank = Bank()
# 将账户存入银行
bank.Logon(a)
# 登录
bank.login()