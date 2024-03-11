prices = [1,2,4,2,5,7,2,4,9,0,9]
l = 0
r = 1
maior = 0
while r < len(prices):
    if(prices[l] >= prices[r]):
        l=r
        r+=1
    elif(prices[r] - prices[l] > maior):
        maior = prices[r] - prices[l]
        r+=1
    else:
        r+=1
print (maior)