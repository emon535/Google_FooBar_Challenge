def solution(data, n): 
    # Your code here
    answer =[]
    count = {}
    for j in data:
        if j in count:
          count[j] +=1
        else:
          count[j] =1
    for key, value in count.items():
        if value > n:
            for i in range(value):
                data.remove(key)
    return data