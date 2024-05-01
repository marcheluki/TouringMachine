class Tape(object):
    blank_symbol = " " # Símbolo en blanco (marca el inicio y final de la cinta)
    
    def __init__(self, tape_string=""):
        self.tape = list(tape_string) # Convierte la cadena en una lista de caracteres
        
    def __str__(self):
        s = ""
        for i in range(len(self.tape)):  # Itera por la cinta completa
            s += self.tape[i]  # Añade cada elemento a la cadena
        return s
    
    def __getitem__(self, index):
        if 0 <= index < len(self.tape):  # Checa que el índice sea válido dentro de la longitud de la cinta
            return self.tape[index] # Regresa el valor en el índice
        return self.blank_symbol # Regresa el símbolo en blanco si el índice no es válido

    def __setitem__(self, pos, char):
        if 0 <= pos < len(self.tape):  # Checa que el índice sea válido dentro de la longitud de la cinta
            self.tape[pos] = char # Cambia el valor en el índice
        else:
            # Caso en el que el índice está fuera de la longitud de la cinta
            self.tape.extend([self.blank_symbol] * (pos - len(self.tape) + 1)) # Extiende la cinta con el símbolo en blanco
            self.tape[pos] = char  # Cambia el valor en la nueva posición

class TuringMachine(object):
    # Inicializa la máquina de Turing con la cinta, el estado actual, la función de transición y los estados finales
    def __init__(self, tape="", current_state='init', transition_function=None, final_states=None):
        self.tape = Tape(tape)
        self.current_state = current_state
        self.transition_function = transition_function if transition_function else {}
        self.final_states = final_states if final_states else set()
        self.head = 1  

    # Realiza un paso en la máquina de Turing
    def step(self):
        # Imprime la cinta, el estado actual y la cabeza
        print(f"Cinta actual: ", self.tape, "Estado actual: ", self.current_state, "Valor actual: ", self.head)
        
        char = self.tape[self.head] # Obtiene el valor en la cabeza de la cinta
        action = self.transition_function.get((self.current_state, char)) # Obtiene la acción en la función de transición
        # Si hay una acción en la función de transición, se realiza
        if action:
            self.tape[self.head] = action['write']
            self.current_state = action['next_state']
            self.head += action['move']


    # Ejecuta la máquina de Turing y valida el resultado
    def execute(self):
        while self.current_state not in self.final_states and self.head < len(str(self.tape)):
            self.step()
            if self.current_state == "E":
                break
            elif self.tape[self.head] != "0" and self.tape[self.head] != "1" and self.tape[self.head] != " " and self.tape[self.head] != "x":
                self.current_state = "E"
                break
        
        # Imprime la cinta, el estado actual y la cabeza final
        print(f"Cinta actual: ", self.tape, "Estado actual: ", self.current_state, "Índice actual: ", self.head)

        if self.current_state == "E":
            print("El string tiene distinta cantidad de 0s y 1s.")

        elif self.current_state in self.final_states and self.head == len(str(self.tape)):
            print("El string tiene la misma cantidad de 0s y 1s.")

        elif self.current_state not in self.final_states and self.head >= len(str(self.tape)):
            print("El string tiene distinta cantidad de 0s y 1s.")

        else: 
            print("El string tiene distinta cantidad de 0s y 1s.")

        """
        elif self.current_state in self.final_states and self.head < len(str(self.tape)):
            print("String has more 0s than 1s.")
        elif self.current_state in self.final_states and self.head > len(str(self.tape)):
            print("String has more 1s than 0s.")
        """
        
    # Regresa la cinta como una cadena
    def get_tape(self):
        return str(self.tape)

    

initial_state = {"init"}
final_states = {"final"}
transition_function = {
    ("init", "x"): {"write": "x", "next_state": "init", "move": 1},
    ("init", "0"): {"write": "x", "next_state": "q1", "move": 1},
    ("init", "1"): {"write": "x", "next_state": "q2", "move": 1}, 
    ("init", " "): {"write": " ", "next_state": "final", "move": 1}, 

    ("q1", "x"): {"write": "x", "next_state": "q1", "move": 1},
    ("q1", "0"): {"write": "0", "next_state": "q1", "move": 1},
    ("q1", "1"): {"write": "x", "next_state": "q3", "move": -1}, 
    ("q1", " "): {"write": " ", "next_state": "E", "move": 1}, 

    ("q2", "x"): {"write": "x", "next_state": "q2", "move": 1},
    ("q2", "1"): {"write": "1", "next_state": "q2", "move": 1},
    ("q2", "0"): {"write": "x", "next_state": "q3", "move": -1},
    ("q2", " "): {"write": " ", "next_state": "E", "move": 1}, 

    ("q3", "0"): {"write": "0", "next_state": "q3", "move": -1},
    ("q3", "1"): {"write": "1", "next_state": "q3", "move": -1},
    ("q3", "x"): {"write": "x", "next_state": "q3", "move": -1},
    ("q3", " "): {"write": " ", "next_state": "init", "move": 1}
}

t = TuringMachine(" 001100110 ",
                  current_state="init",
                  final_states=final_states,
                  transition_function=transition_function)

t.execute()
print(t.get_tape())

