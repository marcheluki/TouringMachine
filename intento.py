# Turing Machine that accepts strings with same quantity of 0s and 1s
# NO FUNCIONA CUANDO TIENE MAS 0S QUE 1S
def turing_machine_0n1n(s):
    tape = [None] + list(s) + [None]
    head = 1  # Start after the initial None
    # N 0 0 1 0 N
    while True:
        # Step 1: Move right to find a 0
        # If a 1 is found, move to the right
        while tape[head] != '0' and tape[head] is not None: 
            head += 1
        print(tape)
        print('Head: ', head)
        
        if tape[head] is None:
            # If no 0 is found and head is at None, check for remaining 1's
            head = 1  # Reset to the start of the tape
            while tape[head] != '1' and tape[head] is not None:
                head += 1
            
            if tape[head] is None:
                # If no 1 is found either, the machine accepts the input
                return True
            else:
                # If there are still 1's left, the machine rejects the input
                return False
            print(tape)
        
        # Step 2: Replace 0 with X
        tape[head] = 'X'
        print(tape)
        print('Head: ', head)
        
        # Step 3: Move left to the blank or Y
        while tape[head] not in [None, 'Y']:
            head -= 1
        print(tape)
        print('Head: ', head)
        
        # Step 4: Move right to find a 1
        head += 1
        while tape[head] != '1':
            if tape[head] is None:
                # If no 1 is found, move to the left to find the next 0
                head -= 1
                break
            head += 1
        print(tape)
        print('Head: ', head)
        

        # Step 5: Replace 1 with Y =====> This is the error
        if tape[head] == '1':
            tape[head] = 'Y'
        print(tape)
        print('Head: ', head)
        
        # Step 6: Move left to find X
        while tape[head] != 'X':
            if tape[head] is None:
                # If no X is found, move to the right to find the next 0
                head += 1
                break
            head -= 1
        print(tape)
        print('Head: ', head)

# Si tiene más 0's que 1's, el programa debe rechazar la cadena pero no sucede
s = ['0011', '1100', '0010', '100', '11001']
correct = [True, True, False]
results = [turing_machine_0n1n(i) for i in s]

print(results)
print(correct)
#print(turing_machine_0n1n('100'))


