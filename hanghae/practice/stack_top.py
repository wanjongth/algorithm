top_heights = [6, 9, 5, 7, 4]

# top이 왼쪽으로 레이저를 쏜다 
# <-<-<-<-<-
# [0,0,0,0,4]
#        7,4

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights: #heights의 원소가 없을때까지
        height = heights.pop()
        # [6,9,5,7]
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
                
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!