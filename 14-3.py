def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # (스테이지 번호, 실패율)
        answer.append((i, fail))
        length -= count
        
    # 실패율을 기준으로 스테이지 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    
    return answer