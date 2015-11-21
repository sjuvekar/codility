def solution(A):
    
    A_len = len(A)
    correct_start = 0
    correct_end = A_len - 1
    # Remove monotonically increasing sequence from start
    while correct_start < correct_end and A[correct_start + 1] >= A[correct_start]:
        correct_start += 1

    # Remove monotonically decreasing sequence from end
    while correct_end < correct_start and A[correct_end - 1] >= A[correct_end]:
        correct_end -= 1

    if correct_end - correct_start <= 1:
        return 0

    max_so_far = A[correct_start]
    min_so_far = A[correct_start]
    ans = 0
    for i in range(correct_start, correct_end + 1):
        if A[i] >= max_so_far:
            max_so_far = A[i]
        elif A[i] <= min_so_far:
            min_so_far = A[i]
        else:
            ans = max(ans, A[i] - min_so_far)

    return ans
        
    
