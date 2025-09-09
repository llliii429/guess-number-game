"""用python设计第一个游戏"""

temp=input("不妨猜数字")
guess=int(temp)

if guess==8:
   print("你对了")
   print("没奖励")
else:
    print("猜错了")
    print("不玩了")
