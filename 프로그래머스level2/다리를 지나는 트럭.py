
def solution(bridge_length, weight, truck_weights):
    x = [0]*bridge_length
    answer = 0
    
    while True:
        if truck_weights==[] and sum(x)==0:
            break
        else:
            answer+=1
            print(x)
            if(sum(x)==0):
                answer-=1

            if truck_weights==[]:
                x.append(0)
                del(x[0]) 
            elif sum(x) + truck_weights[0] <= weight:
                x.append(truck_weights[0])
                del(truck_weights[0])
                del(x[0])
            else:
                x.append(0)
                del(x[0]) 

    return answer+1
 
 
bridge_length, weight, truck_weights = 100,100,[10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))

