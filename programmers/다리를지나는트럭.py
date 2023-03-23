def solution(bridge_length, weight, truck_weights):
    count = 0
    trucks_on_bridge = [0] * bridge_length
    while trucks_on_bridge:
        count += 1
        trucks_on_bridge.pop(0)

        if len(truck_weights):
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
        print(f'count : {count}')
        print(f'trucks_on_bridge : {trucks_on_bridge}')
        print('--------------------------')
    return count
    
# test
l = 2
w = 10
tw = [7,4,5,6]

print(solution(l,w,tw))