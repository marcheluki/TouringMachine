# Works for 0n1n
def turing_machine_0n1n(s):
    tape = [None] + list(s) + [None]  # Set up the tape
    head = 1  # Start at the beginning of the string
    
    while True:
        # Step 1: Find the next 0
        while tape[head] != '0' and tape[head] is not None:
            head += 1
        
        if tape[head] is None:  # No more 0's to pair
            # Check for unmarked 1's
            head = 1  # Reset to start
            while tape[head] not in ['1', None]:
                head += 1
            return tape[head] is None  # Accept if no unmarked 1's
        
        # Step 2: Mark 0 as X
        tape[head] = 'X'
        head += 1  # Move right to find 1

        # Step 3: Find the next 1
        while tape[head] != '1' and tape[head] is not None:
            head += 1

        if tape[head] is None:  # No 1 found to pair with the X
            return False  # Reject

        # Step 4: Mark 1 as Y
        tape[head] = 'Y'
        head = 1  # Reset to find the next 0

# Test cases
s = ['0011', '1100', '0010', '100']
results = [turing_machine_0n1n(i) for i in s]
print(results)
