
print('''
    1.**创建英雄**
    2.**查看英雄信息**
    3.**修改英雄信息**
    4.**删除英雄**
    5.**退出系统**
    ''')
# 创建英雄函数
def create_hero(hero_list):
    hero_name = input("请输入英雄名称：")
    hero_volume = input("请输入英雄血量：")
    hero_power = input("请输入英雄攻击力：")
    hero_info = {"name":hero_name,"volume":hero_volume,"power":hero_power}
    print(f"创建成功！英雄名称为：{hero_name},英雄血量为：{hero_volume},英雄攻击力为：{hero_power}")
    hero_list.append(hero_info)
    return hero_list

# 查找英雄函数
def find_hero(hero_list):
    for i in hero_list:
        if res == i["name"]:
            print(f"英雄{res}的信息为{i}")
    print("没有找到要查找的英雄")
    return hero_list

# 修改函数
def change_hero(hero_list):
    for i in hero_list:
        if res == i["name"]:
            volume = input("请输入修改后的英雄血量：")
            i["volume"] = volume
            print(f"修改后的英雄信息为：{hero_list}")
    print("没有找到要修改的英雄")
    return hero_list


# 删除的函数
def delete_hero(hero_list, hero_name):
    for i in hero_list:
        if res == i["name"]:
            hero_list.remove(i)
            print(f"删除之后的所有英雄数据信息为：{hero_list}")
            return hero_list   # 找到的时候直接终止

    print("没有找到要删除的英雄")
    return hero_list

hero_list = []
while True:
    res = input("请输入数字，选择需要完成的操作：")
    if res == "1":
        print("创建英雄")
        create_hero(hero_list)
    elif res == "2":
        res = input("请输入需要查找的英雄名称：")
        find_hero(hero_list)
    elif res == "3":
        res = input("请输入需要修改的英雄名称：")
        change_hero(hero_list)

    elif res == "4":
        res = input("请输入需要删除的英雄信息：")
        delete_hero(hero_list, res)

    else:
        print("退出系统")
        break
