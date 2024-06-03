############################# 此代码只起到备注作用，与实际数据库结构并不完全相同#########################################

import pymysql
# 数据库初始化
# 创建表
connect = pymysql.connect(host="localhost", user="root", password="***", database="***")  # 建立连接
if connect:
    print("连接成功!")

cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
# 创建表及其约束


cursor.execute(
    "create table Staff(Snum  varchar(10) primary key,Sname varchar(20) not null,Ssex varchar(5) check(Ssex in('男','女')),Sage int not null check(Sage>=18),Sseniority int not null check(Sseniority>=0),Sphone varchar(20) not null,Sid varchar(25) not null, Ssalary int check(Ssalary>=0))")
cursor.execute(
    "create table Vendor(Vnum varchar(10) primary key,Vname varchar(10) not null,Vphone varchar(20) not null,Vplace varchar(10) not null)")
#  on delete cascade
cursor.execute(
    "create table Goods(Gnum varchar(10) primary key,Gname varchar(10) not null,Gtype varchar(10) not null,Gprice int check(Gprice>=0),Gbid int check(Gbid>=0),Gstock int check(Gstock>=0),Galarm int check(Galarm>=0), Gplan int check(Gplan>=0),Vnum varchar(10) not null)")
cursor.execute(
    "create table Member(Mnum varchar(10) primary key,Mname varchar(10) not null,Mphone varchar(20) not null,Mdate datetime,Mtotal int check(Mtotal>=0),Mbalance int check(Mbalance>=0),Mpassword varchar(25) not null)")
# on delete set null
cursor.execute(
    "create table Ware(Wnum varchar(10) primary key,Wname varchar(10) not null,Wplace varchar(10) not null,Snum varchar(10) not null)")
cursor.execute(
    "create table Trade(Tnum varchar(10) primary key,Tdate datetime  not null,Snum varchar(10) not null,Gnum varchar(10) not null,Tamount int check(Tamount>=0),Tmoney int check(Tmoney>=0),Mnum varchar(10) not null)")
cursor.execute(
    "create table Infer(Tnum varchar(10) not null,Gnum varchar(10) not null,Iamount int check(Iamount>=1),Imoney int check(Imoney>=0),Idate datetime not null)")
# on delete cascade
cursor.execute(
    "create table Entry(Enum varchar(10) primary key,Gnum varchar(10) not null,Eamount int check(Eamount>=0),Emoney int check(Emoney>=0),Wnum varchar(10) not null,Edate datetime not null,Snum varchar(10) not null)")
cursor.execute(
    "create table Exits(Xnum varchar(10) primary key,Gnum varchar(10) not null,Xamount int check(Xamount>=0),Xmoney int check(Xmoney>=0),Xdate datetime not null,Snum varchar(10) not null)")
cursor.execute(
"create table Check1(Cdate date primary key,Cemergencylighting varchar(10) check(Cemergencylighting in('正常','异常')),Cfire varchar(10) check(Cfire in('正常','异常')),Csmokedetector varchar(10) check(Csmokedetector in('正常','异常')), Cmonitor varchar(10) check(Cmonitor in('正常','异常')), Cfirstaid varchar(10) check(Cfirstaid in('正常','异常')))")
connect.commit()  # 提交
cursor.close()  # 关闭游标
connect.close()



# 创建触发器 满足顾客买商品的一个场景
connect = pymysql.connect(host="localhost", user="root", password="*****", database="*****")  # 建立连接
# 创建光标
cursor = connect.cursor()

#插入触发器：
# 交易购买的商品数量要在库存里减去
cursor.execute(
    "create trigger update_Goods before insert on Trade for each row update Goods set Gstock=Gstock-new.Tamount where Gnum=new.Gnum;")
# 入库商品也要在库存增加
# 退货商品库存增加
# 退货数量小于等于交易数量
# 退货返钱
# 交易要在会员卡的总消费和余额里改变相应的数值
# 出库商品库存减少
# 交易金额大于商品售价乘以交易数量
cursor.execute(
    "create trigger update_Member before insert on Trade for each row update Member set Mtotal=Mtotal+new.Tmoney,Mbalance=Mbalance-new.Tmoney where Mnum=new.Mnum;")
# 删除触发器
# 删除员工，仓库管理员变成默认管理员，交易员工变成默认员工，入库员工变成默认员工，出库员工变成默认员工，不能删除默认员工Sceo
# 删除商品 ，交易被级联删除，退货被级联删除，出库被级联删除，入库被级联删除
# 删除供应商，商品被级联删除
# 删除仓库，入库改成默认仓库，不能删除默认仓库
# 删除会员，交易表级联删除
# 删除交易表，退过货删除退货信息，没退货商品库存增加会员钱被退回
# 删除退货表，商品库存减少，用户付钱


# 更新触发器
# 更新出库表中的出库量，商品库存变化
# 更新入库表中的入库量，商品库存变化

#查询机制
# 商品库存达到警告量，输出警告
# 安全检查异常，输出警告


connect.commit()
cursor.close()
connect.close()

connect = pymysql.connect(host="localhost", user="root", password="***", database="****")  # 建立连接
cursor = connect.cursor()
# 供应商被删除，对应物品都被删除
cursor.execute("alter table Goods add foreign key(Vnum) references Vendor(Vnum) on delete cascade")
cursor.execute("alter table Ware add foreign key(Snum) references Staff(Snum)") #
cursor.execute("alter table Trade add foreign key(Snum) references Staff(Snum)") #
cursor.execute("alter table Trade add foreign key(Gnum) references Goods(Gnum)") #
cursor.execute("alter table Trade add foreign key(Mnum) references Member(Mnum)")
cursor.execute("alter table Infer add foreign key(Tnum) references Trade(Tnum)")
cursor.execute("alter table Infer add foreign key(Gnum) references Goods(Gnum)") #
cursor.execute("alter table Entry add foreign key(Snum) references Staff(Snum)") #

# 退货信息中商品编号和交易流水号要与交易表中的信息对应，建立符合索引
cursor.execute("alter table Exits add foreign key(Snum) references Staff(Snum)") #
cursor.execute("alter table Exits add foreign key(Gnum) references Goods(Gnum)") #



connect.commit()
# 关闭数据库连接，防止泄露
connect.close()


########################################################################################################

