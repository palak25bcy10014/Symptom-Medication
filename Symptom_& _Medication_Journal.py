# Symptom & Medication Journal
health = [] 

def add_item():
    name = input("Enter medication or symptom name : ")
    category = input("Enter category (Medication/Symptom): ") 
    health.append({"name": name, "info": category, "occurrences": 0}) 
    print("Item added to journal!\n")

def log_occurrence():
    if not health:
        print("No item tracked yet.\n")
        return
    
    print("\n--- Health Items ---")
    for i, item in enumerate(health, 1):
               print(f"{i}. {item['name']} ({item['info']}) - Total Count: {item['occurrences']}")
    
    try:
        idx = int(input("Enter number to log occurrence (Take Medication / Record Symptom): "))
        if 1 <= idx <= len(health):
            health[idx-1]['occurrences'] += 1
            print(f"Logged event for {health[idx-1]['name']}!\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def view_summary():
    if not health:
        print("No records found.\n")
        return
    print("\n--- Journal Summary ---")
    for item in health:
        print(f"{item['name']} | {item['info']} | Total Events: {item['occurrences']}")
    print()

def menu():
    while True:
        print("===== Symptom & Med Journal =====")
        print("1. Add New Item")
        print("2. Log Occurrence (Take Medication/Record Symptom)")
        print("3. View Summary")
        print("4. Exit")
        ch = input("Enter choice: ")
        if ch == '1':
            add_item()
        elif ch == '2':
            log_occurrence()
        elif ch == '3':
            view_summary()
        elif ch == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == '__main__':
    menu()
