import random
# 62, 69, 58
def Class():#随机数生成函数
    l_all = []
    for i in range(0, 20):#初始化所有人都来了
        l_temp = []
        for j in range(0, 90):
            l_temp.append(0)
        l_all.append(l_temp)

    Count = random.randint(5, 8)
    l_student = []
    while(len(l_student) < Count):
        x = random.randint(0, 89)
        if x not in l_student:
            l_student.append(x)
            l_class = []
            while(len(l_class) < 16):
                y = random.randint(0, 19)
                if y not in l_class:
                    l_class.append(y)
                    l_all[y][x] = 1
    for i in range(0, 20):
        Count = random.randint(0, 3)
        while(Count > 0):
            x = random.randint(0, 89)
            if l_all[i][x] == 0:
                l_all[i][x] = 1
                Count = Count - 1
    return l_all
def init():#随机数生成初始化函数
    l_all = []
    for i in range(0, 5):
        l_all.append(Class())
    return l_all
def solve(l_all, every_num):
    last_ans = 0; last_num = every_num * 5
    for i in range(0, 5):
        test = l_all[i]
        ans = []
        fail = []; succeed = []
        for j in range(0, every_num):
            if test[0][j] == 1:
                ans.append(j)
                fail.append(0)
                succeed.append(1)
                last_ans = last_ans + 1
        for j in range(1, 20):
            for k in range(0, len(ans)):
                if succeed[k] > 16 or fail[k] > 4:
                    continue
                if test[j][ans[k]] == 1:
                    succeed[k] = succeed[k] + 1
                    last_ans = last_ans + 1
                    last_num = last_num + 1
                else:
                    fail[k] = fail[k] + 1
                    last_num = last_num + 1
    E = last_ans / last_num
    #print("num = {}, E = {}".format(every_num, E))
    return E
def main():
    every_num = 1
    for i in range(0, 90):
        ave = 0
        for j in range(0, 90):
            ave = ave + solve(init(), every_num)
        ave = ave / 90
        print("ave is {} when num is {}".format(ave, every_num))
        every_num = every_num + 1
main()
