import pymysql
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk


# 全局变量保存当前登录的用户信息
current_user = None


# 数据库连接函数
def db_connect():
    return pymysql.connect(host="localhost", user="root", password="Agao113311", database="dbtest", charset="utf8")


# 登录界面
def login():
    def authenticate():
        global current_user
        username = entry_username.get()
        password = entry_password.get()

        try:
            # 连接数据库
            connection = db_connect()
            with connection.cursor() as cursor:
                # SQL 查询语句
                sql = "SELECT Snum FROM Staff WHERE Snum = %s"
                cursor.execute(sql, (username,))
                result = cursor.fetchone()
                if result:
                    expected_password = result[0] + 'open'  # 从数据库获取的用户名加上 'open'
                    if password == expected_password:
                        current_user = username
                        messagebox.showinfo("登录成功", "欢迎使用商城信息管理系统！")
                        root.destroy()  # 登录成功后销毁登录窗口
                        mainpage()  # 主界面函数需要实现
                    else:
                        messagebox.showerror("登录失败", "用户名或密码错误！")
                else:
                    messagebox.showerror("登录失败", "用户名或密码错误！")
        except Exception as e:
            messagebox.showerror("登录失败", f"数据库错误: {e}")
        finally:
            connection.close()

    root = tk.Tk()
    root.title("登录")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("im10.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    entry_width = 30
    # entry_height = 1
    entry_x = (1000 - entry_width * 10) // 2
    entry_y = 300
    button_width = 10
    # button_height = 1
    button_x = (1000 - button_width * 10) // 2
    button_y = 450

    tk.Label(root, text="管理员登录", font=('default', 30), relief="groove").place(x=entry_x + 40, y=entry_y - 140)
    tk.Label(canvas, text="用户名", bg="white", relief="groove").place(x=entry_x + 60, y=entry_y - 40)
    entry_username = tk.Entry(canvas)
    entry_username.place(x=entry_x + 60, y=entry_y)

    tk.Label(canvas, text="密码", bg="white", relief="groove").place(x=entry_x + 60, y=entry_y + 40)
    entry_password = tk.Entry(canvas, show='*')
    entry_password.place(x=entry_x + 60, y=entry_y + 80)

    tk.Button(root, text="登录", command=authenticate, width=button_width, bd=5).place(x=button_x - 10, y=button_y)

    root.mainloop()






# 主界面
def mainpage():

    def navigate_to_add():
        root.destroy()
        all_add()

    def navigate_to_delete():
        root.destroy()
        all_del()

    def navigate_to_update():
        root.destroy()
        all_upd()

    def navigate_to_select():
        root.destroy()
        all_sel()

    root = tk.Tk()
    root.title("首页")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = (1000 - entry_width*10) // 2  # 水平居中
    entry_y = 300  # 垂直位置
    button_width = 15
    button_height = 1

    tk.Label(root, text="选择您的操作", bg="white", font=('default', 30), relief="groove").place(x=entry_x-20+25, y=entry_y-170)
    tk.Button(root, text="添加信息", command=navigate_to_add, width=button_width,  bd=5).place(x=entry_x+60, y=entry_y-50)
    tk.Button(root, text="删除信息", command=navigate_to_delete, width=button_width, bd=5).place(x=entry_x+60, y=entry_y+40)
    tk.Button(root, text="修改信息", command=navigate_to_update, width=button_width,  bd=5).place(x=entry_x+60, y=entry_y+130)
    tk.Button(root, text="查询信息", command=navigate_to_select, width=button_width, bd=5).place(x=entry_x+60, y=entry_y+220)

    root.mainloop()


# 选择添加界面
def all_add():
    def navigate_to_staff_add():
        root.destroy()
        Staff_add()

    def navigate_to_goods_add():
        root.destroy()
        Goods_add()

    def navigate_to_member_add():
        root.destroy()
        Member_add()

    def navigate_to_vendor_add():
        root.destroy()
        Vendor_add()

    def navigate_to_ware_add():
        root.destroy()
        Ware_add()

    def navigate_to_infer_add():
        root.destroy()
        Infer_add()

    def navigate_to_trade_add():
        root.destroy()
        Trade_add()

    def navigate_to_entry_add():
        root.destroy()
        Entry_add()

    def navigate_to_exits_add():
        root.destroy()
        Exits_add()

    def navigate_to_check1_add():
        root.destroy()
        Check1_add()

    # 根据需要添加更多按钮
    root = tk.Tk()
    root.title("添加信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
    # entry_height = 1
    entry_x = 300  # 水平居中
    entry_y = 155  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="请选择添加信息类型", bg="white", font=('default', 30),  relief="groove").place(x=entry_x-3, y=entry_y-30)
    tk.Button(root, text="员工信息添加 ", command=navigate_to_staff_add, bd=5).place(x=entry_x, y=entry_y+90)
    tk.Button(root, text="商品信息添加 ", command=navigate_to_goods_add, bd=5).place(x=entry_x, y=entry_y+160)
    tk.Button(root, text="安全信息添加 ", command=navigate_to_check1_add, bd=5).place(x=entry_x, y=entry_y+230)
    tk.Button(root, text="仓库信息添加 ", command=navigate_to_ware_add, bd=5).place(x=entry_x, y=entry_y+300)
    tk.Button(root, text="供应商信息添加", command=navigate_to_vendor_add, bd=5).place(x=entry_x, y=entry_y+370)
    tk.Button(root, text="退货信息添加 ", command=navigate_to_infer_add, bd=5).place(x=entry_x+250, y=entry_y+90)
    tk.Button(root, text="会员信息添加 ", command=navigate_to_member_add, bd=5).place(x=entry_x+250, y=entry_y+160)
    tk.Button(root, text="交易信息添加 ", command=navigate_to_trade_add, bd=5).place(x=entry_x+250, y=entry_y+230)
    tk.Button(root, text="入库信息添加 ", command=navigate_to_entry_add, bd=5).place(x=entry_x+250, y=entry_y+300)
    tk.Button(root, text="出库信息添加 ", command=navigate_to_exits_add, bd=5).place(x=entry_x+250, y=entry_y+370)

    # 添加更多按钮

    tk.Button(root, text="返回", command=lambda: [root.destroy(), mainpage()], bd=5, width = button_width, height = button_height).place(x=entry_x+125, y=entry_y+460)

    root.mainloop()



# 选择删除界面
def all_del():
    def navigate_to_staff_del():
        root.destroy()
        Staff_del()

    def navigate_to_goods_del():
        root.destroy()
        Goods_del()

    def navigate_to_member_del():
        root.destroy()
        Member_del()

    def navigate_to_vendor_del():
        root.destroy()
        Vendor_del()

    def navigate_to_ware_del():
        root.destroy()
        Ware_del()

    def navigate_to_infer_del():
        root.destroy()
        Infer_del()

    def navigate_to_trade_del():
        root.destroy()
        Trade_del()



    def navigate_to_check1_del():
        root.destroy()
        Check1_del()


    root = tk.Tk()
    root.title("删除信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
    # entry_height = 1
    entry_x = 300  # 水平居中
    entry_y = 155  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="请选择删除信息类型", bg="white", font=('default', 30), relief="groove").place(x=entry_x - 3,
                                                                                              y=entry_y - 30)
    tk.Button(root, text="员工信息删除 ", command=navigate_to_staff_del, bd=5).place(x=entry_x,
                                                                                                       y=entry_y + 90)
    tk.Button(root, text="商品信息删除 ", command=navigate_to_goods_del, bd=5).place(x=entry_x,
                                                                                                       y=entry_y + 160)
    tk.Button(root, text="安全信息删除 ", command=navigate_to_check1_del, bd=5).place(x=entry_x,
                                                                                                        y=entry_y + 230)
    tk.Button(root, text="仓库信息删除 ", command=navigate_to_ware_del, bd=5).place(x=entry_x,
                                                                                                      y=entry_y + 300)
    tk.Button(root, text="供应商信息删除", command=navigate_to_vendor_del, bd=5).place(x=entry_x+250,
                                                                                                        y=entry_y + 300)
    tk.Button(root, text="退货信息删除 ", command=navigate_to_infer_del, bd=5).place(x=entry_x + 250,
                                                                                                       y=entry_y + 90)
    tk.Button(root, text="会员信息删除 ", command=navigate_to_member_del, bd=5).place(x=entry_x + 250,
                                                                                                        y=entry_y + 160)
    tk.Button(root, text="交易信息删除 ", command=navigate_to_trade_del, bd=5).place(x=entry_x + 250,
                                                                                                       y=entry_y + 230)

    # 删除更多按钮

    tk.Button(root, text="返回", command=lambda: [root.destroy(), mainpage()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 125, y=entry_y + 410)

    root.mainloop()


# 选择修改界面
def all_upd():
    def navigate_to_staff_upd():
        root.destroy()
        Staff_upd()

    def navigate_to_goods_upd():
        root.destroy()
        Goods_upd()

    def navigate_to_member_upd():
        root.destroy()
        Member_upd()

    def navigate_to_vendor_upd():
        root.destroy()
        Vendor_upd()

    def navigate_to_ware_upd():
        root.destroy()
        Ware_upd()


    def navigate_to_entry_upd():
        root.destroy()
        Entry_upd()

    def navigate_to_exits_upd():
        root.destroy()
        Exits_upd()



    root = tk.Tk()
    root.title("修改信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
    # entry_height = 1
    entry_x = 310  # 水平居中
    entry_y = 155  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="请选择修改信息类型", bg="white", font=('default', 30), relief="groove").place(x=entry_x - 3,
                                                                                              y=entry_y - 30)
    tk.Button(root, text="员工信息修改 ", command=navigate_to_staff_upd, bd=5).place(x=entry_x,
                                                                                                       y=entry_y + 90)
    tk.Button(root, text="商品信息修改 ", command=navigate_to_goods_upd, bd=5).place(x=entry_x,
                                                                                                       y=entry_y + 160)
    tk.Button(root, text="仓库信息修改 ", command=navigate_to_ware_upd, bd=5).place(x=entry_x,
                                                                                                      y=entry_y + 230)
    tk.Button(root, text="供应商信息修改", command=navigate_to_vendor_upd, bd=5).place(x=entry_x,
                                                                                                        y=entry_y + 300)

    tk.Button(root, text="会员信息修改 ", command=navigate_to_member_upd, bd=5).place(x=entry_x + 250,
                                                                                                        y=entry_y + 160)
    tk.Button(root, text="入库信息修改 ", command=navigate_to_entry_upd, bd=5).place(x=entry_x + 250,
                                                                                                       y=entry_y + 230)
    tk.Button(root, text="出库信息修改 ", command=navigate_to_exits_upd, bd=5).place(x=entry_x + 250,
                                                                                                       y=entry_y + 90)

    # 修改更多按钮

    tk.Button(root, text="返回", command=lambda: [root.destroy(), mainpage()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 250,
        y=entry_y + 300)

    root.mainloop()


# 选择查询界面
def all_sel():
    def navigate_to_staff_sel():
        root.destroy()
        Staff_sel()

    def navigate_to_goods_sel():
        root.destroy()
        Goods_sel()

    def navigate_to_member_sel():
        root.destroy()
        Member_sel()

    def navigate_to_vendor_sel():
        root.destroy()
        Vendor_sel()

    def navigate_to_ware_sel():
        root.destroy()
        Ware_sel()

    def navigate_to_infer_sel():
        root.destroy()
        Infer_sel()

    def navigate_to_trade_sel():
        root.destroy()
        Trade_sel()

    def navigate_to_entry_sel():
        root.destroy()
        Entry_sel()

    def navigate_to_exits_sel():
        root.destroy()
        Exits_sel()

    def navigate_to_check1_sel():
        root.destroy()
        Check1_sel()

    def navigate_to_profit_and_cost_sel():
        root.destroy()
        Profit_and_cost_sel()  # 假设这是处理盈利和成本查询的界面函数

    root = tk.Tk()
    root.title("查询信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
    # entry_height = 1
    entry_x = 300  # 水平居中
    entry_y = 155  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="请选择查询信息类型", bg="white", font=('default', 30), relief="groove").place(x=entry_x - 3,
                                                                                              y=entry_y - 30)
    tk.Button(root, text="员工信息查询 ", command=navigate_to_staff_sel, bd=5).place(x=entry_x,
                                                                                                       y=entry_y + 90)
    tk.Button(root, text="商品信息查询 ", command=navigate_to_goods_sel, bd=5).place(x=entry_x,
                                                                                                       y=entry_y + 160)
    tk.Button(root, text="安全信息查询 ", command=navigate_to_check1_sel, bd=5).place(x=entry_x,
                                                                                                        y=entry_y + 230)
    tk.Button(root, text="仓库信息查询 ", command=navigate_to_ware_sel, bd=5).place(x=entry_x,
                                                                                                      y=entry_y + 300)
    tk.Button(root, text="供应商信息查询", command=navigate_to_vendor_sel, bd=5).place(x=entry_x,
                                                                                                        y=entry_y + 370)
    tk.Button(root, text="退货信息查询 ", command=navigate_to_infer_sel, bd=5).place(x=entry_x + 250,
                                                                                                       y=entry_y + 90)
    tk.Button(root, text="会员信息查询 ", command=navigate_to_member_sel, bd=5).place(x=entry_x + 250,
                                                                                                        y=entry_y + 160)
    tk.Button(root, text="交易信息查询 ", command=navigate_to_trade_sel, bd=5).place(x=entry_x + 250,
                                                                                                       y=entry_y + 230)
    tk.Button(root, text="入库信息查询 ", command=navigate_to_entry_sel, bd=5).place(x=entry_x + 250,
                                                                                                       y=entry_y + 300)
    tk.Button(root, text="出库信息查询 ", command=navigate_to_exits_sel, bd=5).place(x=entry_x + 250,
                                                                                                       y=entry_y + 370)
    tk.Button(root, text="成本和盈利", command=navigate_to_profit_and_cost_sel, bd=5, width = button_width, height = button_height).place(x=entry_x + 45, y=entry_y + 460)

    # 查询更多按钮

    tk.Button(root, text="返回", command=lambda: [root.destroy(), mainpage()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 185, y=entry_y + 460)

    root.mainloop()


# 员工信息添加界面
def Staff_add():
    def add_staff():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Staff(Snum, Sname, Ssex, Sage, Sseniority, Sphone, Sid, Ssalary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get(), v8.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("员工信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 135  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加员工信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x+40, y=entry_y - 50)

    labels = ["员工编号", "姓名", "性别", "年龄", "工龄", "电话号", "身份证号", "工资"]
    vars = [tk.StringVar() for _ in range(8)]
    global v1, v2, v3, v4, v5, v6, v7, v8
    v1, v2, v3, v4, v5, v6, v7, v8 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y+57
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=15, height=button_height).place(x=entry_x-20, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=24, bd=3).place(x=entry_x+160, y=entry_y)

    tk.Button(root, text="添加", command=add_staff, width = button_width, height = button_height, bd=5).place(x=entry_x-15, y=entry_y+80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], width = button_width, height = button_height, bd=5).place(x=entry_x+227, y=entry_y+80)

    root.mainloop()


# 商品信息添加界面（类似于员工信息添加界面）
def Goods_add():
    def add_goods():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Goods(Gnum, Gname, Gtype, Gprice, Gbid, Gstock, Galarm, Gplan, Vnum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get(), v8.get(), v9.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("商品信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
    # entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 122  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加商品信息", font=("default", 30), bg="white", relief="groove").place(x=entry_x+60, y=entry_y - 50)

    labels = ["商品编号", "商品名称", "商品类别", "商品价格", "商品成本", "库存量", "告警库存", "计划库存", "供应商编号"]
    vars = [tk.StringVar() for _ in range(9)]
    global v1, v2, v3, v4, v5, v6, v7, v8, v9
    v1, v2, v3, v4, v5, v6, v7, v8, v9 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 53
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=15, height=button_height).place(x=entry_x-20, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x+170, y=entry_y)

    tk.Button(root, text="添加", command=add_goods, bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y+60)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], bd=5, width = button_width, height = button_height).place(x=entry_x+238, y=entry_y+60)

    root.mainloop()


def Vendor_add():
    def add_vendor():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Vendor(Vnum,Vname,Vphone,Vplace) VALUES (%s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("供应商信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加供应商信息", font=("default", 30), bg="white", relief="groove").place(x=entry_x +40, y=entry_y - 50)

    labels = ["供应商编号", "供应商名称", "供应商电话", "供应商地址"]
    vars = [tk.StringVar() for _ in range(4)]
    global v1, v2, v3, v4
    v1, v2, v3, v4 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 75
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=16, height=button_height).place(
            x=entry_x-20, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x + 190, y=entry_y)

    tk.Button(root, text="添加", command=add_vendor, bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], bd=5, width = button_width, height = button_height).place(x=entry_x + 238,
                                                                                                  y=entry_y + 80)

    root.mainloop()



def Ware_add():
    def add_ware():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Ware(Wnum,Wname,Wplace,Snum) VALUES (%s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("仓库信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
   # entry_width = 30
   # entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 160  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加仓库信息", font=("default", 30), bg="white", relief="groove").place(x=entry_x+55 , y=entry_y - 50)

    labels = ["仓库编号", "仓库名称", "仓库地址", "仓库管理员编号"]
    vars = [tk.StringVar() for _ in range(4)]
    global v1, v2, v3, v4
    v1, v2, v3, v4 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 75
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=20, height=button_height).place(
            x=entry_x-20, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x + 190, y=entry_y)

    tk.Button(root, text="添加", command=add_ware,  bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], bd=5, width = button_width, height = button_height).place(x=entry_x + 238,
                                                                                                  y=entry_y + 80)

    root.mainloop()




def Exits_add():
    def add_exits():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Exits(Xnum,Gnum,Xamount,Remarks,Xdate,Snum) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("出库信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
    # entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 160  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加出库信息", font=("default", 30), bg="white", relief="groove").place(x=entry_x + 60, y=entry_y - 50)

    labels = ["出库单编号", "商品编号", "出库量", "备注信息", "出库日期", "出库员编号"]
    vars = [tk.StringVar() for _ in range(6)]
    global v1, v2, v3, v4, v5, v6
    v1, v2, v3, v4, v5, v6 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 60
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x-10, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x + 180, y=entry_y)

    tk.Button(root, text="添加", command=add_exits, bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], bd=5, width = button_width, height = button_height).place(x=entry_x + 238,
                                                                                                  y=entry_y + 80)

    root.mainloop()




def Member_add():
    def add_member():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Member(Mnum, Mname, Mphone, Mdate, Mtotal, Mbalance, Mpassword) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("会员信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 135  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加会员信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 55, y=entry_y - 50)

    labels = ["会员卡号", "会员姓名", "会员电话", "注册日期", "累计金额", "卡内余额", "会员密码"]
    vars = [tk.StringVar() for _ in range(7)]
    global v1, v2, v3, v4, v5, v6, v7
    v1, v2, v3, v4, v5, v6, v7 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 60
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=15, height=button_height).place(
            x=entry_x-10, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x + 180, y=entry_y)

    tk.Button(root, text="添加", command=add_member,bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], bd=5, width = button_width, height = button_height).place(x=entry_x + 238,
                                                                                                  y=entry_y + 80)

    root.mainloop()


def Entry_add():
    def add_entry():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Entry(Enum, Gnum, Eamount, Remarks, Wnum, Edate, Snum) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("入库信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 135  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加入库信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 65, y=entry_y - 60)

    labels = ["入库单编号", "商品编号", "入库量", "备注信息", "仓库编号", "入库日期", "入库员编号"]
    vars = [tk.StringVar() for _ in range(7)]
    global v1, v2, v3, v4, v5, v6, v7
    v1, v2, v3, v4, v5, v6, v7 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 60
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x-10, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x + 180, y=entry_y)

    tk.Button(root, text="添加", command=add_entry, bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()],bd=5, width = button_width, height = button_height).place(x=entry_x + 238,
                                                                                                  y=entry_y + 80)

    root.mainloop()


def Trade_add():
    def add_trade():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Trade(Tnum, Tdate, Snum, Gnum, Tamount, Tmoney, Mnum) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("商品交易信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
   #  entry_width = 30
    # entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 135  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加商品交易信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x+20 , y=entry_y - 50)

    labels = ["交易流水号", "交易日期", "员工编号", "商品编号", "交易数量", "交易金额", "会员卡号"]
    vars = [tk.StringVar() for _ in range(7)]
    global v1, v2, v3, v4, v5, v6, v7
    v1, v2, v3, v4, v5, v6, v7 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 60
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=15, height=button_height).place(
            x=entry_x-10, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x + 180, y=entry_y)

    tk.Button(root, text="添加", command=add_trade, bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], bd=5, width = button_width, height = button_height).place(x=entry_x + 238,
                                                                                                  y=entry_y + 80)

    root.mainloop()


def Check1_add():
    def add_check1():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Check1(Cdate, Cemergencylighting, Cfire, Csmokedetector, Cmonitor, Cfirstaid) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("安全信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
   # entry_width = 30
   # entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 135  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加安全信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 65, y=entry_y - 50)

    labels = ["检查日期", "应急照明状态", "消防设备状态", "烟雾探测器状态", "监控设备状态", "急救设备状态"]
    vars = [tk.StringVar() for _ in range(6)]
    global v1, v2, v3, v4, v5, v6
    v1, v2, v3, v4, v5, v6 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 65
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=20, height=button_height).place(
            x=entry_x-15, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x + 190, y=entry_y)

    tk.Button(root, text="添加", command=add_check1, bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], bd=5, width = button_width, height = button_height).place(x=entry_x + 238,
                                                                                                  y=entry_y + 80)

    root.mainloop()


def Infer_add():
    def add_infer():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "INSERT INTO Infer(Tnum, Gnum, Iamount, Imoney, Idate) VALUES (%s, %s, %s, %s, %s)"
        values = (v1.get(), v2.get(), v3.get(), v4.get(), v5.get())
        try:
            cursor.execute(sql, values)
            connect.commit()
            messagebox.showinfo("提示", "信息添加成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息添加失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("退货信息添加")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 315  # 水平居中
    entry_y = 135  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="添加退货信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 65, y=entry_y - 50)

    labels = ["交易流水号", "商品编号", "退货数量", "退款金额", "退货日期"]
    vars = [tk.StringVar() for _ in range(5)]
    global v1, v2, v3, v4, v5
    v1, v2, v3, v4, v5 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 70
        tk.Label(root, text=f"请输入{label}：", bg="white", relief="groove", width=16, height=button_height).place(
            x=entry_x-10, y=entry_y)
        tk.Entry(root, textvariable=vars[i], width=25, bd=3).place(x=entry_x + 180, y=entry_y)

    tk.Button(root, text="添加", command=add_infer, bd=5, width = button_width, height = button_height).place(x=entry_x, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_add()], bd=5, width = button_width, height = button_height).place(x=entry_x + 238,
                                                                                                  y=entry_y + 80)

    root.mainloop()

####################################################del###########################################
##################################################################################################

def Staff_del():
    def del_staff():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "DELETE FROM Staff WHERE Snum = %s"
        value = v1.get()
        try:
            cursor.execute(sql, (value,))
            connect.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("错误", "未找到对应的员工编号")
            else:
                messagebox.showinfo("提示", "信息删除成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息删除失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("删除员工信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 290  # 水平居中
    entry_y = 225  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="删除员工信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 75,
                                                                                           y=entry_y - 80)

    tk.Label(root, text="请输入员工编号：", bg="white", relief="groove", width=15, height=button_height).place(
        x=entry_x +10, y=entry_y + 70)

    global v1
    v1 = tk.StringVar()
    tk.Entry(root, textvariable=v1, width=25, bd=3).place(x=entry_x + 200, y=entry_y + 70)

    tk.Button(root, text="删除", command=del_staff, bd=5, width = button_width, height = button_height).place(x=entry_x+25, y=entry_y + 180)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_del()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 238, y=entry_y + 180)

    root.mainloop()



# 商品信息添加界面（类似于员工信息添加界面）
def Goods_del():
    def del_goods():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "DELETE FROM Goods WHERE Gnum = %s"
        value = v1.get()
        try:
            cursor.execute(sql, (value,))
            connect.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("错误", "未找到对应的商品编号")
            else:
                messagebox.showinfo("提示", "信息删除成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息删除失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("删除商品信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 290  # 水平居中
    entry_y = 225  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="删除商品信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 75,
                                                                                           y=entry_y - 80)

    tk.Label(root, text="请输入商品编号：", bg="white", relief="groove", width=15, height=button_height).place(
        x=entry_x +10, y=entry_y + 70)

    global v1
    v1 = tk.StringVar()
    tk.Entry(root, textvariable=v1, width=25, bd=3).place(x=entry_x + 200, y=entry_y + 70)

    tk.Button(root, text="删除", command=del_goods, bd=5 , width = button_width, height = button_height).place(x=entry_x+25, y=entry_y + 180)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_del()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 238, y=entry_y + 180)

    root.mainloop()


def Vendor_del():
    def del_vendor():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "DELETE FROM Vendor WHERE Vnum = %s"
        value = v1.get()
        try:
            cursor.execute(sql, (value,))
            connect.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("错误", "未找到对应的供应商编号")
            else:
                messagebox.showinfo("提示", "信息删除成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息删除失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("删除供应商信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 290  # 水平居中
    entry_y = 225  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="删除供应商信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x +70,
                                                                                           y=entry_y - 80)

    tk.Label(root, text="请输入供应商编号：", bg="white", relief="groove", width=17, height=button_height).place(
        x=entry_x +30, y=entry_y + 70)

    global v1
    v1 = tk.StringVar()
    tk.Entry(root, textvariable=v1, width=25, bd=3).place(x=entry_x + 190, y=entry_y + 70)

    tk.Button(root, text="删除", command=del_vendor, bd=5, width = button_width, height = button_height).place(x=entry_x+40, y=entry_y + 180)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_del()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 258, y=entry_y + 180)

    root.mainloop()


def Ware_del():
    def del_ware():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "DELETE FROM Ware WHERE Wnum = %s"
        value = v1.get()
        try:
            cursor.execute(sql, (value,))
            connect.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("错误", "未找到对应的仓库编号")
            else:
                messagebox.showinfo("提示", "信息删除成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息删除失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("删除仓库信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 290  # 水平居中
    entry_y = 245  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="删除仓库信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 75,
                                                                                           y=entry_y - 80)

    tk.Label(root, text="请输入仓库编号：", bg="white", relief="groove", width=17, height=button_height).place(
        x=entry_x , y=entry_y + 70)

    global v1
    v1 = tk.StringVar()
    tk.Entry(root, textvariable=v1, width=25, bd=3).place(x=entry_x + 190, y=entry_y + 70)

    tk.Button(root, text="删除", command=del_ware, bd=5, width = button_width, height = button_height).place(x=entry_x+20, y=entry_y + 180)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_del()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 238, y=entry_y + 180)

    root.mainloop()




def Member_del():
    def del_member():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "DELETE FROM Member WHERE Mnum = %s"
        value = v1.get()
        try:
            cursor.execute(sql, (value,))
            connect.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("错误", "未找到对应的会员卡号")
            else:
                messagebox.showinfo("提示", "信息删除成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息删除失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("删除会员信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 290  # 水平居中
    entry_y = 255  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="删除会员信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 75,
                                                                                           y=entry_y - 80)

    tk.Label(root, text="请输入会员卡号：", bg="white", relief="groove", width=17, height=button_height).place(
        x=entry_x +10, y=entry_y + 70)

    global v1
    v1 = tk.StringVar()
    tk.Entry(root, textvariable=v1, width=25, bd=3).place(x=entry_x + 210, y=entry_y + 70)

    tk.Button(root, text="删除", command=del_member, bd=5, width = button_width, height = button_height).place(x=entry_x+25, y=entry_y + 180)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_del()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 238, y=entry_y + 180)

    root.mainloop()



def Trade_del():
    def del_trade():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "DELETE FROM Trade WHERE Tnum = %s"
        value = v1.get()
        try:
            cursor.execute(sql, (value,))
            connect.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("错误", "未找到对应的交易流水号")
            else:
                messagebox.showinfo("提示", "信息删除成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息删除失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("删除交易信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 290  # 水平居中
    entry_y = 240  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="删除交易信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 85,
                                                                                           y=entry_y - 80)

    tk.Label(root, text="请输入交易流水号：", bg="white", relief="groove", width=17, height=button_height).place(
        x=entry_x +20, y=entry_y + 70)

    global v1
    v1 = tk.StringVar()
    tk.Entry(root, textvariable=v1, width=25, bd=3).place(x=entry_x + 210, y=entry_y + 70)

    tk.Button(root, text="删除", command=del_trade, bd=5, width = button_width, height = button_height).place(x=entry_x+40, y=entry_y + 180)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_del()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 238, y=entry_y + 180)

    root.mainloop()



def Check1_del():
    def del_check1():
        connect = db_connect()
        cursor = connect.cursor()
        sql = "DELETE FROM Check1 WHERE Cdate = %s"
        value = v1.get()
        try:
            cursor.execute(sql, (value,))
            connect.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("错误", "未找到对应的检查日期")
            else:
                messagebox.showinfo("提示", "信息删除成功")
        except Exception as e:
            connect.rollback()
            messagebox.showerror("错误", f"信息删除失败: {e}")
        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("删除安全信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 290  # 水平居中
    entry_y = 245  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="删除安全信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 85,
                                                                                           y=entry_y - 80)

    tk.Label(root, text="请输入检查日期：", bg="white", relief="groove", width=17, height=button_height).place(
        x=entry_x +20, y=entry_y + 70)

    global v1
    v1 = tk.StringVar()
    tk.Entry(root, textvariable=v1, width=25, bd=3).place(x=entry_x + 210, y=entry_y + 70)

    tk.Button(root, text="删除", command=del_check1, bd=5, width = button_width, height = button_height).place(x=entry_x+40, y=entry_y + 180)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_del()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 243, y=entry_y + 180)

    root.mainloop()


def Infer_del():
    def del_infer():
        connect = db_connect()
        cursor = connect.cursor()

        # 禁用自动提交，以启用事务控制
        connect.autocommit = False

        # 获取用户输入的交易流水号
        value = v1.get()

        try:
            # 先查询需要从Infer表删除的记录相关信息
            cursor.execute("SELECT Imoney, Iamount, Gnum, Tnum FROM Infer WHERE Tnum = %s", (value,))
            record = cursor.fetchone()

            if record is None:
                messagebox.showerror("错误", "未找到对应的交易流水号")
                return

            imoney, iamount, gnum, tnum = record

            # 删除Infer表中的记录
            cursor.execute("DELETE FROM Infer WHERE Tnum = %s", (value,))

            # 更新Goods表中的Gstock字段
            cursor.execute("UPDATE Goods SET Gstock = Gstock - %s WHERE Gnum = %s", (iamount, gnum))

            # 从Trade表中获取会员编号Mnum
            cursor.execute("SELECT Mnum FROM Trade WHERE Tnum = %s", (tnum,))
            mnum_result = cursor.fetchone()
            if mnum_result:
                mnum = mnum_result[0]
                # 更新Member表中的Mtotal和Mbalance字段
                cursor.execute("UPDATE Member SET Mtotal = Mtotal + %s, Mbalance = Mbalance - %s WHERE Mnum = %s",
                               (imoney, imoney, mnum))

            # 提交事务
            connect.commit()
            messagebox.showinfo("提示", "信息删除成功")

        except Exception as e:
            # 事务回滚
            connect.rollback()
            messagebox.showerror("错误", f"信息删除失败: {e}")

        finally:
            # 关闭游标和连接
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("删除退货信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 290  # 水平居中
    entry_y = 245  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="删除退货信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 85,
                                                                                           y=entry_y - 80)

    tk.Label(root, text="请输入交易流水号：", bg="white", relief="groove", width=17, height=button_height).place(
        x=entry_x +20, y=entry_y + 70)

    global v1
    v1 = tk.StringVar()
    tk.Entry(root, textvariable=v1, width=25, bd=3).place(x=entry_x + 210, y=entry_y + 70)

    tk.Button(root, text="删除", command=del_infer, bd=5, width = button_width, height = button_height).place(x=entry_x+45, y=entry_y + 190)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_del()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 245, y=entry_y + 190)

    root.mainloop()



#####################################################upd#############################################
#####################################################################################################

def Staff_upd():
    def upd_staff():
        connect = db_connect()
        cursor = connect.cursor()

        sql_parts = []
        values = []

        # 获取薪资更新的勾选状态一次，并存储在变量中
        update_salary = cb5_var.get()

        if cb1_var.get():
            sql_parts.append("Sname = %s")
            values.append(v2.get())
        if cb2_var.get():
            sql_parts.append("Sage = %s")
            values.append(v3.get())
        if cb3_var.get():
            sql_parts.append("Sseniority = %s")
            values.append(v4.get())
        if cb4_var.get():
            sql_parts.append("Sphone = %s")
            values.append(v5.get())
        if cb5_var.get():
            sql_parts.append("Ssalary = %s")
            values.append(v6.get())



        if sql_parts:
            cursor.execute("SELECT COUNT(*) FROM Staff WHERE Snum = %s", (v1.get(),))
            if cursor.fetchone()[0] == 0:
                messagebox.showerror("错误", "不存在的员工编号")
                cursor.close()
                connect.close()
                return

            # 添加员工编号到参数列表的末尾
            values.append(v1.get())
            # 调用存储过程，并传递update_salary变量
            sql = f"CALL upd_staff_and_check_salary(%s, %s, %s, %s, %s, %s, %s)"
            try:
                cursor.execute(sql, [v1.get(), v2.get() if cb1_var.get() else None, v3.get() if cb2_var.get() else None,
                                     v4.get() if cb3_var.get() else None, v5.get() if cb4_var.get() else None,
                                     v6.get() if update_salary else None,
                                     update_salary])
                connect.commit()
                if cursor.rowcount == 0:
                    messagebox.showerror("错误", "修改相同信息")
                else:
                    messagebox.showinfo("提示", "信息修改成功")
            except Exception as e:
                connect.rollback()
                messagebox.showerror("错误", f"信息修改失败: {e}")

            cursor.close()
            connect.close()
        else:
            messagebox.showwarning("警告", "没有选择任何字段进行修改")
            cursor.close()
            connect.close()


    root = tk.Tk()
    root.title("修改员工信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 330  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="修改员工信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 60,
                                                                                           y=entry_y - 50)

    labels = ["请输入员工编号", "员工姓名", "员工年龄", "员工工龄", "员工电话", "工资"]
    vars = [tk.StringVar() for _ in range(6)]
    global v1, v2, v3, v4, v5, v6
    v1, v2, v3, v4, v5, v6 = vars

    # Checkbutton variables
    global cb1_var, cb2_var, cb3_var, cb4_var, cb5_var
    cb1_var = tk.BooleanVar()
    cb2_var = tk.BooleanVar()
    cb3_var = tk.BooleanVar()
    cb4_var = tk.BooleanVar()
    cb5_var = tk.BooleanVar()


    for i, label in enumerate(labels):
        entry_y = entry_y + 65
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=15, height=button_height).place(
            x=entry_x - 30, y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 140, y=entry_y)
        if i > 0:  # 添加Checkbutton作为开关
            cb = tk.Checkbutton(root, text="修改", variable=[cb1_var, cb2_var, cb3_var, cb4_var, cb5_var][i - 1])
            cb.place(x=entry_x + 365, y=entry_y)

    tk.Button(root, text="修改", command=upd_staff, bd=5, width = button_width, height = button_height).place(x=entry_x-15, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_upd()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 245, y=entry_y + 80)

    root.mainloop()



def Goods_upd():
    def upd_goods():
        connect = db_connect()
        cursor = connect.cursor()

        sql_parts = []
        values = []

        if cb1_var.get():
            sql_parts.append("Gname = %s")
            values.append(v2.get())
        if cb2_var.get():
            sql_parts.append("Gprice = %s")
            values.append(v3.get())
        if cb3_var.get():
            sql_parts.append("Gbid = %s")
            values.append(v4.get())
        if cb4_var.get():
            sql_parts.append("Gstock = %s")
            values.append(v5.get())
        if cb5_var.get():
            sql_parts.append("Galarm = %s")
            values.append(v6.get())
        if cb6_var.get():
            sql_parts.append("Gplan = %s")
            values.append(v7.get())


        values.append(v1.get())

        if sql_parts:
            sql = f"UPDATE Goods SET {', '.join(sql_parts)} WHERE Gnum = %s"
            try:
                cursor.execute(sql, values)
                connect.commit()
                if cursor.rowcount == 0:
                    messagebox.showerror("错误", "未找到对应的商品编号或修改相同内容")
                else:
                    messagebox.showinfo("提示", "信息修改成功")
            except Exception as e:
                connect.rollback()
                messagebox.showerror("错误", f"信息修改失败: {e}")
        else:
            messagebox.showwarning("警告", "没有选择任何字段进行修改")

        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("修改商品信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="修改商品信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 95,
                                                                                           y=entry_y - 50)

    labels = ["请输入商品编号", "商品名称", "商品售价", "商品进价", "库存量", "告警量", "计划库存量"]
    vars = [tk.StringVar() for _ in range(7)]
    global v1, v2, v3, v4, v5, v6, v7
    v1, v2, v3, v4, v5, v6, v7 = vars

    # Checkbutton variables
    global cb1_var, cb2_var, cb3_var, cb4_var, cb5_var, cb6_var
    cb1_var = tk.BooleanVar()
    cb2_var = tk.BooleanVar()
    cb3_var = tk.BooleanVar()
    cb4_var = tk.BooleanVar()
    cb5_var = tk.BooleanVar()
    cb6_var = tk.BooleanVar()

    for i, label in enumerate(labels):
        entry_y = entry_y + 60
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 190, y=entry_y)
        if i > 0:  # 添加Checkbutton作为开关
            cb = tk.Checkbutton(root, text="修改", variable=[cb1_var, cb2_var, cb3_var, cb4_var, cb5_var, cb6_var][i - 1])
            cb.place(x=entry_x + 440, y=entry_y)

    tk.Button(root, text="修改", command=upd_goods, bd=5, width = button_width, height = button_height).place(x=entry_x+30, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_upd()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()


def Vendor_upd():
    def upd_vendor():
        connect = db_connect()
        cursor = connect.cursor()

        sql_parts = []
        values = []

        if cb1_var.get():
            sql_parts.append("Vname = %s")
            values.append(v2.get())
        if cb2_var.get():
            sql_parts.append("Vphone = %s")
            values.append(v3.get())
        if cb3_var.get():
            sql_parts.append("Vplace = %s")
            values.append(v4.get())


        values.append(v1.get())

        if sql_parts:
            sql = f"UPDATE Vendor SET {', '.join(sql_parts)} WHERE Vnum = %s"
            try:
                cursor.execute(sql, values)
                connect.commit()
                if cursor.rowcount == 0:
                    messagebox.showerror("错误", "未找到对应的供应商编号或修改相同内容")
                else:
                    messagebox.showinfo("提示", "信息修改成功")
            except Exception as e:
                connect.rollback()
                messagebox.showerror("错误", f"信息修改失败: {e}")
        else:
            messagebox.showwarning("警告", "没有选择任何字段进行修改")

        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("修改供应商信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="修改供应商信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 80,
                                                                                           y=entry_y - 50)

    labels = ["请输入供应商编号", "供应商名称", "供应商电话", "供应商地址"]
    vars = [tk.StringVar() for _ in range(4)]
    global v1, v2, v3, v4
    v1, v2, v3, v4 = vars

    # Checkbutton variables
    global cb1_var, cb2_var, cb3_var
    cb1_var = tk.BooleanVar()
    cb2_var = tk.BooleanVar()
    cb3_var = tk.BooleanVar()



    for i, label in enumerate(labels):
        entry_y = entry_y + 75
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 190, y=entry_y)
        if i > 0:  # 添加Checkbutton作为开关
            cb = tk.Checkbutton(root, text="修改", variable=[cb1_var, cb2_var, cb3_var][i - 1])
            cb.place(x=entry_x + 440, y=entry_y)

    tk.Button(root, text="修改", command=upd_vendor, bd=5, width = button_width, height = button_height).place(x=entry_x+20, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_upd()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()



def Ware_upd():
    def upd_ware():
        connect = db_connect()
        cursor = connect.cursor()

        sql_parts = []
        values = []

        if cb1_var.get():
            sql_parts.append("Wname = %s")
            values.append(v2.get())
        if cb2_var.get():
            sql_parts.append("Wplace = %s")
            values.append(v3.get())
        if cb3_var.get():
            sql_parts.append("Snum = %s")
            values.append(v4.get())

        values.append(v1.get())

        if sql_parts:
            sql = f"UPDATE Ware SET {', '.join(sql_parts)} WHERE Wnum = %s"
            try:
                cursor.execute(sql, values)
                connect.commit()
                if cursor.rowcount == 0:
                    messagebox.showerror("错误", "未找到对应的仓库编号或修改相同内容")
                else:
                    messagebox.showinfo("提示", "信息修改成功")
            except Exception as e:
                connect.rollback()
                messagebox.showerror("错误", f"信息修改失败: {e}")
        else:
            messagebox.showwarning("警告", "没有选择任何字段进行修改")

        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("修改仓库信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="修改仓库信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 90,
                                                                                            y=entry_y - 50)

    labels = ["请输入仓库编号", "仓库名称", "仓库地址", "仓库管理员编号"]
    vars = [tk.StringVar() for _ in range(4)]
    global v1, v2, v3, v4
    v1, v2, v3, v4 = vars

    # Checkbutton variables
    global cb1_var, cb2_var, cb3_var
    cb1_var = tk.BooleanVar()
    cb2_var = tk.BooleanVar()
    cb3_var = tk.BooleanVar()

    for i, label in enumerate(labels):
        entry_y = entry_y + 75
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=15, height=button_height).place(
            x=entry_x , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 190, y=entry_y)
        if i > 0:  # 添加Checkbutton作为开关
            cb = tk.Checkbutton(root, text="修改", variable=[cb1_var, cb2_var, cb3_var][i - 1])
            cb.place(x=entry_x + 440, y=entry_y)

    tk.Button(root, text="修改", command=upd_ware, bd=5, width = button_width, height = button_height).place(x=entry_x+20, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_upd()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()


def Exits_upd():
    def upd_exits():
        connect = db_connect()
        cursor = connect.cursor()

        sql_parts = []
        values = []

        if cb1_var.get():
            sql_parts.append("Xamount = %s")
            values.append(v2.get())
        if cb2_var.get():
            sql_parts.append("Remarks = %s")
            values.append(v3.get())
        if cb3_var.get():
            sql_parts.append("Xdate = %s")
            values.append(v4.get())
        if cb4_var.get():
            sql_parts.append("Snum = %s")
            values.append(v5.get())

        values.append(v1.get())

        if sql_parts:
            sql = f"UPDATE Exits SET {', '.join(sql_parts)} WHERE Xnum = %s"
            try:
                cursor.execute(sql, values)
                connect.commit()
                if cursor.rowcount == 0:
                    messagebox.showerror("错误", "未找到对应的出库单编号或修改相同内容")
                else:
                    messagebox.showinfo("提示", "信息修改成功")
            except Exception as e:
                connect.rollback()
                messagebox.showerror("错误", f"信息修改失败: {e}")
        else:
            messagebox.showwarning("警告", "没有选择任何字段进行修改")

        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("修改出库信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="修改出库信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 90,
                                                                                           y=entry_y - 50)

    labels = ["请输入出库单编号", "出库量", "备注信息", "出库日期", "出库员编号"]
    vars = [tk.StringVar() for _ in range(5)]
    global v1, v2, v3, v4, v5
    v1, v2, v3, v4, v5 = vars

    # Checkbutton variables
    global cb1_var, cb2_var, cb3_var, cb4_var
    cb1_var = tk.BooleanVar()
    cb2_var = tk.BooleanVar()
    cb3_var = tk.BooleanVar()
    cb4_var = tk.BooleanVar()

    for i, label in enumerate(labels):
        entry_y = entry_y + 75
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 190, y=entry_y)
        if i > 0:  # 添加Checkbutton作为开关
            cb = tk.Checkbutton(root, text="修改", variable=[cb1_var, cb2_var, cb3_var, cb4_var][i - 1])
            cb.place(x=entry_x + 440, y=entry_y)

    tk.Button(root, text="修改", command=upd_exits, bd=5, width = button_width, height = button_height).place(x=entry_x+20, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_upd()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()




def Member_upd():
    def upd_member():
        connect = db_connect()
        cursor = connect.cursor()

        sql_parts = []
        values = []

        if cb1_var.get():
            sql_parts.append("Mname = %s")
            values.append(v2.get())
        if cb2_var.get():
            sql_parts.append("Mphone = %s")
            values.append(v3.get())
        if cb3_var.get():
            sql_parts.append("Mtotal = %s")
            values.append(v4.get())
        if cb4_var.get():
            sql_parts.append("Mbalance = %s")
            values.append(v5.get())
        if cb5_var.get():
            sql_parts.append("Mpassword = %s")
            values.append(v6.get())

        values.append(v1.get())

        if sql_parts:
            sql = f"UPDATE Member SET {', '.join(sql_parts)} WHERE Mnum = %s"
            try:
                cursor.execute(sql, values)
                connect.commit()
                if cursor.rowcount == 0:
                    messagebox.showerror("错误", "未找到对应的会员卡号或修改相同内容")
                else:
                    messagebox.showinfo("提示", "信息修改成功")
            except Exception as e:
                connect.rollback()
                messagebox.showerror("错误", f"信息修改失败: {e}")
        else:
            messagebox.showwarning("警告", "没有选择任何字段进行修改")

        cursor.close()
        connect.close()

    root = tk.Tk()
    root.title("修改会员信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="修改会员信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 95,
                                                                                           y=entry_y - 50)

    labels = ["请输入会员卡号", "会员姓名", "会员电话", "累计金额", "卡内余额", "会员密码"]
    vars = [tk.StringVar() for _ in range(6)]
    global v1, v2, v3, v4, v5, v6
    v1, v2, v3, v4, v5, v6 = vars

    # Checkbutton variables
    global cb1_var, cb2_var, cb3_var, cb4_var, cb5_var
    cb1_var = tk.BooleanVar()
    cb2_var = tk.BooleanVar()
    cb3_var = tk.BooleanVar()
    cb4_var = tk.BooleanVar()
    cb5_var = tk.BooleanVar()

    for i, label in enumerate(labels):
        entry_y = entry_y + 65
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 190, y=entry_y)
        if i > 0:  # 添加Checkbutton作为开关
            cb = tk.Checkbutton(root, text="修改", variable=[cb1_var, cb2_var, cb3_var, cb4_var, cb5_var][i - 1])
            cb.place(x=entry_x + 440, y=entry_y)

    tk.Button(root, text="修改", command=upd_member, bd=5, width = button_width, height = button_height).place(x=entry_x+30, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_upd()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()


def Entry_upd():
    def upd_entry():
        connect = db_connect()
        cursor = connect.cursor()

        sql_parts = []
        values = []

        if cb1_var.get():
            sql_parts.append("Eamount = %s")
            values.append(v2.get())
        if cb2_var.get():
            sql_parts.append("Rmarks = %s")
            values.append(v3.get())
        if cb3_var.get():
            sql_parts.append("Edate = %s")
            values.append(v4.get())
        if cb4_var.get():
            sql_parts.append("Snum = %s")
            values.append(v5.get())

        values.append(v1.get())

        if sql_parts:
            sql = f"UPDATE Entry SET {', '.join(sql_parts)} WHERE Enum = %s"
            try:
                cursor.execute(sql, values)
                connect.commit()
                if cursor.rowcount == 0:
                    messagebox.showerror("错误", "未找到对应的入库单编号或修改相同内容")
                else:
                    messagebox.showinfo("提示", "信息修改成功")
            except Exception as e:
                connect.rollback()
                messagebox.showerror("错误", f"信息修改失败: {e}")
        else:
            messagebox.showwarning("警告", "没有选择任何字段进行修改")

        cursor.close()
        connect.close()


    root = tk.Tk()
    root.title("修改入库信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="修改入库信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 95,
                                                                                           y=entry_y - 50)

    labels = ["请输入入库单编号", "入库量", "备注信息", "入库日期", "入库员编号"]
    vars = [tk.StringVar() for _ in range(5)]
    global v1, v2, v3, v4, v5
    v1, v2, v3, v4, v5 = vars

    # Checkbutton variables
    global cb1_var, cb2_var, cb3_var, cb4_var
    cb1_var = tk.BooleanVar()
    cb2_var = tk.BooleanVar()
    cb3_var = tk.BooleanVar()
    cb4_var = tk.BooleanVar()

    for i, label in enumerate(labels):
        entry_y = entry_y + 65
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 190, y=entry_y)
        if i > 0:  # 添加Checkbutton作为开关
            cb = tk.Checkbutton(root, text="修改", variable=[cb1_var, cb2_var, cb3_var, cb4_var][i - 1])
            cb.place(x=entry_x + 440, y=entry_y)

    tk.Button(root, text="修改", command=upd_entry, bd=5, width = button_width, height = button_height).place(x=entry_x+20, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_upd()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()


################################################################SEL#############################
##########################################################################################################


def Staff_sel():
    def sel_staff():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Staff WHERE Snum = %s"
            cursor.execute(sql, (v1.get(),))
            result = cursor.fetchone()

            if result:
                v2.set(result[1])
                v3.set(result[2])
                v4.set(result[3])
                v5.set(result[4])
                v6.set(result[5])
                v7.set(result[6])
                v8.set(result[7])
            else:
                messagebox.showerror("错误", "未找到对应的员工编号")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询员工信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
    # entry_height = 1
    entry_x = 283  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询员工信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 90, y=entry_y - 50)

    labels = ["请输入员工编号", "员工姓名", "员工性别", "员工年龄", "员工工龄", "员工电话", "身份证号", "工资"]
    vars = [tk.StringVar() for _ in range(8)]
    global v1, v2, v3, v4, v5, v6, v7, v8
    v1, v2, v3, v4, v5, v6, v7, v8 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 50
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=26, bd=3)
        entry.place(x=entry_x + 200, y=entry_y)

    tk.Button(root, text="查询", command=sel_staff, bd=5, width = button_width, height = button_height).place(x=entry_x+10, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_sel()], bd=5 , width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()

# 商品信息添加界面（类似于员工信息添加界面）
def Goods_sel():
    def sel_goods():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Goods WHERE Gnum = %s"
            cursor.execute(sql, (g1.get(),))
            result = cursor.fetchone()

            if result:
                g2.set(result[1])
                g3.set(result[2])
                g4.set(result[3])
                g5.set(result[4])
                g6.set(result[5])
                g7.set(result[6])
                g8.set(result[7])
                g9.set(result[8])
                if int(g6.get()) <= int(g7.get()):
                    messagebox.showinfo("库存警告", "库存不足，请尽快补货！")
            else:
                messagebox.showerror("错误", "未找到对应的商品编号")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询商品信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
   #  entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 100  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询商品信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 90, y=entry_y - 50)

    labels = ["请输入商品编号", "商品名称", "商品类别", "商品售价", "商品进价", "库存量", "告警量", "计划库存量", "供应商编号"]
    vars = [tk.StringVar() for _ in range(9)]
    global g1, g2, g3, g4, g5, g6, g7, g8, g9
    g1, g2, g3, g4, g5, g6, g7, g8, g9 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 50
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=15, height=button_height).place(
            x=entry_x+10 , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 200, y=entry_y)

    tk.Button(root, text="查询", command=sel_goods, bd=5, width = button_width, height = button_height).place(x=entry_x+15, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda:  [root.destroy(), all_sel()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 273, y=entry_y + 80)

    root.mainloop()

def Vendor_sel():
    def sel_vendor():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Vendor WHERE Vnum = %s"
            cursor.execute(sql, (v1.get(),))
            result = cursor.fetchone()

            if result:
                v2.set(result[1])
                v3.set(result[2])
                v4.set(result[3])
            else:
                messagebox.showerror("错误", "未找到对应的供应商编号")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询供应商信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
   #  entry_height = 1
    entry_x = 281  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询供应商信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 75, y=entry_y - 50)

    labels = ["请输入供应商编号", "供应商名称", "供应商电话", "供应商地址"]
    vars = [tk.StringVar() for _ in range(4)]
    global v1, v2, v3, v4
    v1, v2, v3, v4 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 70
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x , y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=26, bd=3)
        entry.place(x=entry_x + 205, y=entry_y)

    tk.Button(root, text="查询", command=sel_vendor, bd=5, width = button_width, height = button_height).place(x=entry_x+10, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_sel()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()

def Ware_sel():
    def sel_ware():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            # 执行视图查询
            sql = """
                    SELECT DISTINCT GoodsNumber, GoodsName, VendorName, PurchasePrice, Stock
                    FROM WarehouseGoodsView
                    WHERE GoodsNumber IN (
                        SELECT DISTINCT Gnum FROM Entry WHERE Wnum = %s
                    )
                    """
            cursor.execute(sql, (w1.get(),))
            results = cursor.fetchall()

            if results:
                # 清空之前的结果
                for row in tree.get_children():
                    tree.delete(row)
                # 插入新的结果
                for row in results:
                    tree.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("信息", "未找到对应的入库商品信息")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询仓库信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 281  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询仓库信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 105,y=entry_y - 50)

    # 单个输入框
    tk.Label(root, text="请输入仓库编号：", bg="white", relief="groove", width=17, height=button_height).place(x=entry_x + 30, y=entry_y + 70)

    w1 = tk.StringVar()
    entry = tk.Entry(root, textvariable=w1, width=25, bd=3)
    entry.place(x=entry_x + 220, y=entry_y + 70)

    tk.Button(root, text="查询", command=sel_ware, bd=5, width=button_width, height=button_height).place(x=entry_x + 20,
                                                                                                       y=entry_y + 480)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_sel()], bd=5, width=button_width,
              height=button_height).place(
        x=entry_x + 298, y=entry_y + 480)

    # 创建Treeview来显示查询结果
    columns = ("GoodsNumber", "GoodsName", "VendorName", "PurchasePrice", "Stock")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("GoodsNumber", text="商品编号")
    tree.heading("GoodsName", text="商品名称")
    tree.heading("VendorName", text="供货商名称")
    tree.heading("PurchasePrice", text="进价")
    tree.heading("Stock", text="库存")

    tree.column("GoodsNumber", width=100)
    tree.column("GoodsName", width=150)
    tree.column("VendorName", width=150)
    tree.column("PurchasePrice", width=100)
    tree.column("Stock", width=100)
    # 放置Treeview和滚动条
    tree.place(x=entry_x - 100, y=entry_y + 120, width=650, height=300)

    root.mainloop()

Ware_sel()
def Exits_sel():
    def sel_exits():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Exits WHERE Xnum = %s"
            cursor.execute(sql, (x1.get(),))
            result = cursor.fetchone()

            if result:
                x2.set(result[1])
                x3.set(result[2])
                x4.set(result[3])
                x5.set(result[4])
                x6.set(result[5])
            else:
                messagebox.showerror("错误", "未找到对应的出库单编号")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询出库信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 284  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询出库信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 90, y=entry_y-50 )

    labels = ["请输入出库单编号", "商品编号", "出库量", "备注信息", "出库日期", "出库员编号"]
    vars = [tk.StringVar() for _ in range(6)]
    global x1, x2, x3, x4, x5, x6
    x1, x2, x3, x4, x5, x6 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 50
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x +10, y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 200, y=entry_y)

    tk.Button(root, text="查询", command=sel_exits, bd=5, width = button_width, height = button_height).place(x=entry_x+20, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(),all_sel() ], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()




def Member_sel():
    def sel_member():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Member WHERE Mnum = %s"
            cursor.execute(sql, (m1.get(),))
            result = cursor.fetchone()

            if result:
                m2.set(result[1])
                m3.set(result[2])
                m4.set(result[3])
                m5.set(result[4])
                m6.set(result[5])
                m7.set(result[6])
            else:
                messagebox.showerror("错误", "未找到对应的会员卡号")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询会员信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    # entry_width = 30
   #  entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询会员信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 95, y=entry_y - 50)

    labels = ["请输入会员卡号", "会员姓名", "会员电话", "注册日期", "累计金额", "卡内余额", "会员密码"]
    vars = [tk.StringVar() for _ in range(7)]
    global m1, m2, m3, m4, m5, m6, m7
    m1, m2, m3, m4, m5, m6, m7 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 50
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=15, height=button_height).place(
            x=entry_x +10, y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 200, y=entry_y)

    tk.Button(root, text="查询", command=sel_member, bd=5, width = button_width, height = button_height).place(x=entry_x+15, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(),all_sel()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()



def Entry_sel():
    def sel_entry():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Entry WHERE Enum = %s"
            cursor.execute(sql, (e1.get(),))
            result = cursor.fetchone()

            if result:
                e2.set(result[1])
                e3.set(result[2])
                e4.set(result[3])
                e5.set(result[4])
                e6.set(result[5])
                e7.set(result[6])
            else:
                messagebox.showerror("错误", "未找到对应的入库单编号")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询入库信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 283  # 水平居中
    entry_y = 130  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询入库信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 83,
                                                                                           y=entry_y - 50)

    labels = ["请输入入库单编号", "商品编号", "入库量", "备注信息", "仓库编号", "入库日期", "入库员编号"]
    vars = [tk.StringVar() for _ in range(7)]
    global e1, e2, e3, e4, e5, e6, e7
    e1, e2, e3, e4, e5, e6, e7 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 60
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x +10, y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 200, y=entry_y)

    tk.Button(root, text="查询", command=sel_entry, bd=5,  width = button_width, height = button_height).place(x=entry_x+15, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_sel()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 268, y=entry_y + 80)

    root.mainloop()



def Trade_sel():
    def sel_trade():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Trade WHERE Tnum = %s"
            cursor.execute(sql, (t1.get(),))
            result = cursor.fetchone()

            if result:
                t2.set(result[1])
                t3.set(result[2])
                t4.set(result[3])
                t5.set(result[4])
                t6.set(result[5])
                t7.set(result[6])
            else:
                messagebox.showerror("错误", "未找到对应的交易流水号")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询交易信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询交易信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 85, y=entry_y - 50)

    labels = ["请输入交易流水号", "交易日期", "员工编号", "商品编号", "交易数量", "交易金额", "会员卡号"]
    vars = [tk.StringVar() for _ in range(7)]
    global t1, t2, t3, t4, t5, t6, t7
    t1, t2, t3, t4, t5, t6, t7 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 50
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x +20, y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 210, y=entry_y)

    tk.Button(root, text="查询", command=sel_trade, bd=5, width = button_width, height = button_height).place(x=entry_x+35, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(),all_sel()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()



def Check1_sel():
    def sel_check1():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Check1 WHERE Cdate = %s"
            cursor.execute(sql, (c1.get(),))
            result = cursor.fetchone()

            if result:
                c2.set(result[1])
                c3.set(result[2])
                c4.set(result[3])
                c5.set(result[4])
                c6.set(result[5])
                # Check for abnormal conditions
                if any(status != '正常' for status in result[1:5]):
                    messagebox.showerror("警告", "安全设备存在异常，请尽快检修！")
            else:
                messagebox.showerror("错误", "未找到对应的检查日期")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询检查信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询检查信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 90, y=entry_y - 50)

    labels = ["请输入检查日期", "应急照明状态", "消防设备状态", "烟雾探测器状态", "监控设备状态", "急救设备状态"]
    vars = [tk.StringVar() for _ in range(6)]
    global c1, c2, c3, c4, c5, c6
    c1, c2, c3, c4, c5, c6 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 60
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=15, height=button_height).place(
            x=entry_x +20, y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 210, y=entry_y)

    tk.Button(root, text="查询", command=sel_check1, bd=5, width = button_width, height = button_height).place(x=entry_x+25, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(),all_sel()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()




def Infer_sel():
    def sel_infer():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            sql = "SELECT * FROM Infer WHERE Tnum = %s"
            cursor.execute(sql, (v1.get(),))
            result = cursor.fetchone()

            if result:
                v2.set(result[1])
                v3.set(result[2])
                v4.set(result[3])
                v5.set(result[4])
            else:
                messagebox.showerror("错误", "未找到对应的交易流水号")
        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询退货信息")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("resized_bg3.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_width = 30
    entry_height = 1
    entry_x = 278  # 水平居中
    entry_y = 150  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询退货信息", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 90, y=entry_y - 50)

    labels = ["请输入交易流水号", "商品编号", "退货数量", "退款金额", "退货日期"]
    vars = [tk.StringVar() for _ in range(5)]
    global v1, v2, v3, v4, v5
    v1, v2, v3, v4, v5 = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 70
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x +20, y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 210, y=entry_y)

    tk.Button(root, text="查询", command=sel_infer, bd=5, width = button_width, height = button_height).place(x=entry_x+30, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_sel()], bd=5, width = button_width, height = button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()


def Profit_and_cost_sel():
    def sel_profit_and_cost():
        connect = db_connect()
        cursor = connect.cursor()

        try:
            # Query for total cost
            sql_cost = "SELECT SUM(Gbid * Gstock) FROM goods"
            cursor.execute(sql_cost)
            total_cost = cursor.fetchone()[0]

            # Query for total trade amount
            sql_trade_total = "SELECT SUM(Tmoney) FROM trade"
            cursor.execute(sql_trade_total)
            trade_total = cursor.fetchone()[0]

            # Query for total refund
            sql_refund_total = "SELECT SUM(Imoney) FROM Infer"
            cursor.execute(sql_refund_total)
            refund_total = cursor.fetchone()[0]

            # Query for total trade cost
            sql_trade_cost = """
                       SELECT SUM(g.Gbid * t.Tamount)
                       FROM trade t
                       JOIN goods g ON t.Gnum = g.Gnum
                   """
            cursor.execute(sql_trade_cost)
            trade_cost_total = cursor.fetchone()[0]

            sql_refund_cost = """
                           SELECT SUM(g.Gbid * i.Iamount)
                           FROM Infer i
                           JOIN goods g ON i.Gnum = g.Gnum
                       """
            cursor.execute(sql_refund_cost)
            refund_cost_total = cursor.fetchone()[0]

            # Calculate total profit
            total_profit = trade_total - trade_cost_total - refund_total + refund_cost_total

            if total_cost is not None:
                v_cost.set(total_cost)
            else:
                v_cost.set("0")

            if total_profit is not None:
                v_profit.set(total_profit)
            else:
                v_profit.set("0")

        except Exception as e:
            messagebox.showerror("错误", f"信息查询失败: {e}")
        finally:
            cursor.close()
            connect.close()

    root = tk.Tk()
    root.title("查询总成本和总盈利")
    root.geometry("1000x750")

    # 加载背景图片
    background_image = Image.open("cr_im11.png")
    background_photo = ImageTk.PhotoImage(background_image)

    # 创建 Canvas 小部件并设置背景图片
    canvas = tk.Canvas(root, width=1000, height=750)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # 计算输入框和按钮的位置，使其位于窗口中心
    entry_x = 278  # 水平居中
    entry_y = 230  # 垂直位置
    button_width = 12
    button_height = 1

    tk.Label(root, text="查询总成本和总盈利", bg="white", font=("default", 30), relief="groove").place(x=entry_x + 30,
                                                                                              y=entry_y - 37)

    labels = ["总成本", "总盈利"]
    vars = [tk.StringVar() for _ in range(2)]
    global v_cost, v_profit
    v_cost, v_profit = vars

    for i, label in enumerate(labels):
        entry_y = entry_y + 70
        tk.Label(root, text=f"{label}：", bg="white", relief="groove", width=17, height=button_height).place(
            x=entry_x + 20, y=entry_y)
        entry = tk.Entry(root, textvariable=vars[i], width=25, bd=3)
        entry.place(x=entry_x + 210, y=entry_y)

    tk.Button(root, text="查询", command=sel_profit_and_cost, bd=5, width=button_width, height=button_height).place(
        x=entry_x + 30, y=entry_y + 80)
    tk.Button(root, text="返回", command=lambda: [root.destroy(), all_sel()], bd=5, width=button_width,
              height=button_height).place(
        x=entry_x + 278, y=entry_y + 80)

    root.mainloop()



if __name__ == '__main__':
    login()

