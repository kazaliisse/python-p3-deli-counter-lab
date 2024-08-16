# lib/deli_counter.py

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        for index, person in enumerate(katz_deli):
            line_status += f" {index + 1}. {person}"
        print(line_status)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")

# Test your functions with the example usage
if __name__ == "__main__":
    katz_deli = []

    take_a_number(katz_deli, "Ada") 
    take_a_number(katz_deli, "Grace") 
    take_a_number(katz_deli, "Kent") 

    line(katz_deli) 

    now_serving(katz_deli)

    line(katz_deli) 

    take_a_number(katz_deli, "Matz") 

    line(katz_deli) 

    now_serving(katz_deli) 

    line(katz_deli) 
