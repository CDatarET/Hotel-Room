# cook your dish here
cases = int(input())
for c in range(cases):
    inputs = input().split()
    people = int(inputs[1])
    peak = people
    
    room = list(map(int, input().split()))
    
    for i in range(int(inputs[0])):
        people = people + room[i]
        if(peak <= people):
            peak = people
        
    print(peak)
