def turing_machine(s):
    tape = list(s)
    head = 0
    
    try:
        while True:
            # Move to the first unmarked 0 or 1
            while tape[head] not in ['0', '1']:
                head += 1
            
            current = tape[head]
            mark = 'X' if current == '0' else 'Y'
            
            # Find the opposite character and mark both
            found = False
            search_head = head + 1
            while search_head < len(tape):
                if tape[search_head] == ('1' if current == '0' else '0'):
                    tape[search_head] = 'Y' if current == '0' else 'X'
                    tape[head] = mark
                    found = True
                    break
                search_head += 1
            
            if not found:
                return False  # Unmatched 0 or 1 found
            
            # Reset head to start to look for next unmarked 0 or 1
            head = 0

    except IndexError:
        # When head goes out of tape's bounds
        pass

    # Check if all are marked correctly without any remaining 0's or 1's
    return all(x in ['X', 'Y'] for x in tape)

# Test examples
test_strings = ['0011', '0101', '000111', '000', '111000', '101010', '1001']
results = {s: turing_machine(s) for s in test_strings}
print(results)
