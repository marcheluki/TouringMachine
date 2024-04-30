def turing_machine(s):
    tape = list(s)
    head = 0
    
    try:
        while True: 
            while tape[head] not in ['0', '1']: # Move to the first unmarked 0 or 1
                head += 1 # Move head to the right
            
            current = tape[head] # Get the current character
            mark = 'X' if current == '0' else 'Y' # Mark the current character
            found = False  # Find the opposite character and mark both
            search_head = head + 1 # Start searching from the next cell
            while search_head < len(tape): # Search for the opposite character
                if tape[search_head] == ('1' if current == '0' else '0'): # Found opposite character
                    tape[search_head] = 'Y' if current == '0' else 'X' # Mark the opposite character
                    tape[head] = mark   # Mark the current character
                    found = True # Marked both
                    break # Exit the loop
                search_head += 1 # Move head to the right
            
            if not found: # If no opposite character found
                return False  # Unmatched 0 or 1 found
            
            head = 0 # Reset head to start to look for next unmarked 0 or 1

    except IndexError:
        pass # End of the tape reached

    return all(x in ['X', 'Y'] for x in tape) # Check if all are marked correctly without any remaining 0's or 1's

# Test examples
test_strings = ['0011', '0101', '0000111', '000', '111000', '10110','11' , '1', '01110']
results = {s: turing_machine(s) for s in test_strings}
print(results)