import random

def Class():  # 生成随机数
    allstudent = []
    for i in range(0, 20):  # 初始化数据
        temp = []
        for j in range(0, 90):
            temp.append(0)
        allstudent.append(temp)

    Count = random.randint(5, 8)
    l_student = []
    while (len(l_student) < Count):
        x = random.randint(0, 89)
        if x not in l_student:
            l_student.append(x)
            classes = []
            while (len(classes) < 16):
                y = random.randint(0, 19)
                if y not in classes:
                    classes.append(y)
                    allstudent[y][x] = 1
    for i in range(0, 20):
        Count = random.randint(0, 3)
        while (Count > 0):
            x = random.randint(0, 89)
            if allstudent[i][x] == 0:
                allstudent[i][x] = 1
                Count = Count - 1
    return allstudent


def init():  # 随机数生成初始化函数
    all = []
    for i in range(0, 5):
        all.append(Class())
    return all

def solve(all, every_num, other):
    lastans = 0
    lastnum = every_num * 5
    for i in range(0, 5):     # 五门课程
        test = all[i]
        ans = []
        fail = []
        succeed = []
        for j in range(0, every_num):
            if test[0][j] == 1:
                ans.append(j)
                fail.append(0)
                succeed.append(1)
                lastans = lastans + 1
        for j in range(1, 20):
            t = 0
            for k in range(0, len(ans)):
                if succeed[k] > 16 or fail[k] > 4:
                    continue
                t = t + 1
                if test[j][ans[k]] == 1:
                    succeed[k] = succeed[k] + 1
                    lastans = lastans + 1
                    lastnum = lastnum + 1
                else:
                    fail[k] = fail[k] + 1
                    lastnum = lastnum + 1
            extra = other
            if t < 3:
                while(extra > 0):
                    x = random.randint(0, 89)
                    if x not in ans:
                        extra = extra - 1
                        ans.append(x)
                        if test[j][x] == 1:
                            succeed.append(1)
                            fail.append(0)
                            lastans = lastans + 1
                            lastnum = lastnum + 1
                        else:
                            succeed.append(20)
                            fail.append(10)
                            lastnum = lastnum + 1
    E = lastans / lastnum
    return E


def main():    # 循环20次，算出E的值
    every_num = 1
    other = 4
    for i in range(0, 90):
        ave = 0
        for j in range(0, 90):
            ave = ave + solve(init(), every_num, other)
        ave = ave / 90
        print("E = {} ".format(ave))
        every_num = every_num + 1
main()
