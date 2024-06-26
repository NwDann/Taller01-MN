
def guessing(N):
    global sequence
    outPut = "Q " + " ".join(map(str, sequence))
    print(outPut)
    prev_correctBits = int(input())
    sys.stdout.flush()
    
    if prev_correctBits < N/2:
        sequence = [1] * N
        prev_correctBits = N - prev_correctBits
    
    for i in range(N):
        sequence[i] = 1 - sequence[i]  # Changing from 0 to 1 and from 1 to 0
        outPut = "Q " + " ".join(map(str, sequence))
        print(outPut)
        correctBits = int(input())
        sys.stdout.flush()
        
        if correctBits == N:
            return True  # Correct sequence
            
        elif correctBits < N and correctBits > prev_correctBits:
            prev_correctBits = correctBits
            
        else:
            sequence[i] = 1 - sequence[i]  # Reversing the change
            if (i == N - 1) and (correctBits == N - 1):
                return True
            
    return False

# ------------------------------MAIN---------------------------------------

import sys

N = int(input())
sequence = [0] * N

flag = guessing(N)

if flag:
    outPut = "A " + " ".join(map(str, sequence))
    print(outPut)
    sys.stdout.flush()
else:
    print("Sequence not guessed")
