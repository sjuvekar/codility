def solution(S):
    max_len = -1
    cur_len = 0
    n_digits = 0
    n_leters = 0
    extra_chars = False

    for c in S:

        cur_len += 1
        # word boundary
        if c == " ":
            if (not extra_chars and n_leters%2 == 0 and n_digits%2 == 1):
                if cur_len > max_len:
                    max_len = cur_len
            cur_len = 0
            n_digits = 0
            n_leters = 0
            extra_chars = False
            
        #digit
        elif c >= '0' and c <= '9':
            n_digits += 1

        #letters
        elif (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            n_leters += 1
        
        #else
        else:
            extra_chars = True

    return max_len
