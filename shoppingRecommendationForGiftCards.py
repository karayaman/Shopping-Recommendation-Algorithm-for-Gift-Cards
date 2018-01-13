#Author: Alper Karayaman

import easygui

def findAll(arr,dp,i,j,cost,answer,temp=[],nr=5):
    if len(answer) == nr:
        return
    if j != 0:
        temp.append((i,j))
    try:
        if not dp[i][j][cost]:
            answer.append(tuple(temp))
        else:
            itself=round(arr[i]*j,1)
            remaining=round(cost-itself,1)
            for k in dp[i][j][cost]:
                findAll(arr,dp,i-1,k,remaining,answer,temp,nr)
    except:
        print("Cost:"+str(cost))
        for key in dp[i][j]:
            print(key)
    if j != 0:
        temp.pop()



def recommend(arr,limit,value,nr):
    cheapest=float("inf")
    dp=[[0]*(limit+1) for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(limit+1):
            dp[i][j]={}
            if i == 0:
                cost=round(arr[i]*j,1)
                if cost >= value:
                    cheapest=min(cheapest,cost)
                dp[i][j][cost]=[]
            else:
                itself=round(arr[i]*j,1)
                if itself >= value:
                    cheapest=min(cheapest,itself)
                    dp[i][j][itself]=[]
                else:
                    for k in range(limit+1):
                        for key in dp[i-1][k]:
                            if key < value:
                                cost=round(key+itself,1)
                                if cost > cheapest:
                                    continue
                                if cost >= value:
                                    cheapest=min(cheapest,cost)
                                if cost in dp[i][j]:
                                    dp[i][j][cost].append(k)
                                else:
                                    dp[i][j][cost]=[k]
    answer=[]
    for i in range(len(arr)):
        for j in range(limit+1):
            if len(answer) == nr:
                return cheapest,answer
            for cost in dp[i][j]:
                if cost == cheapest:
                    findAll(arr,dp,i,j,cost,answer,[],nr)
    return cheapest,answer

class product:
    def __init__(self,data):
        data=data.strip()
        back=-1
        try:
            while data[back] != ' ':
                back-=1
        except:
            print(data)
        self.name=data[:back]
        try:
            self.cost=round(float(data[back:].replace(',','.')),1)
        except ValueError:
            print(data[back:])

data=easygui.textbox("Please enter products.")
currency,value,limit,keywords,nr=easygui.multenterbox(title="Options",fields=["Please enter currency.","Please enter money you want to achieve.","Please enter limit.","Keywords","How many recommendations you want?"],values=["TL",40,3,"Comma seperated","5"])
value=float(value)
limit=int(limit)
keywords=keywords.encode('utf-8').strip()
keywords=keywords.split(',')
nr=int(nr)
products=[]

for line in data.split('\n'):
    line=line.encode('utf-8').strip()
    if line.endswith(currency) and any(keyword in line for keyword in keywords):
        products.append(product(line.rstrip(currency)))

products.sort(key=lambda p:p.cost,reverse=True)

arr=[]
for product in products:
    arr.append(product.cost)

cheapest,answer=recommend(arr,limit,value,nr)
output="Cheapest: "+str(cheapest)+"\n"
for recommendation in answer:
    output+="*************\n"
    for product in recommendation:
        if isinstance(product[0],int):
            output+=str(product[1])+"x "+products[product[0]].name+"\n"
        else:
            for i,j in product:
                output+=str(j)+"x "+products[product[i]].name+"\n"
    output+="*************\n"

easygui.msgbox(output)
