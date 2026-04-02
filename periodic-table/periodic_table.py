import periodictable

def display_element(element):
    print("\n" + "="*40)
    print(f"   ELEMENT DETAILS")
    print("="*40)
    print(f"   Name          : {element.name.capitalize()}")
    print(f"   Symbol        : {element.symbol}")
    print(f"   Atomic No.    : {element.number}")
    print(f"   Atomic Mass   : {element.mass} u")
    print(f"   Density       : {element.density} g/cm³" if element.density else "   Density       : N/A")
    print("="*40 + "\n")

def search_by_symbol(symbol):
    for element in periodictable.elements:
        if element.symbol.lower() == symbol.lower():
            return element
    return None

def search_by_name(name):
    for element in periodictable.elements:
        if element.name.lower() == name.lower():
            return element
    return None

def main():
    print("\n Periodic Table Explorer")
    print("-" * 40)
    print("Search by:")
    print("   1. Atomic Number")
    print("   2. Element Symbol")
    print("   3. Element Name")
    print("   4. List ALL Elements")
    print("-" * 40)

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        try:
            atomic_no = int(input("Enter atomic number (1-118): "))
            if 1 <= atomic_no <= 118:
                display_element(periodictable.elements[atomic_no])
            else:
                print("Atomic number must be between 1 and 118.")
        except ValueError:
            print("Please enter a valid integer.")

    elif choice == "2":
        symbol = input("Enter element symbol (e.g., Fe, Au, H): ").strip()
        element = search_by_symbol(symbol)
        if element:
            display_element(element)
        else:
            print(f"No element found with symbol '{symbol}'.")

    elif choice == "3":
        name = input("Enter element name (e.g., Gold, Carbon): ").strip()
        element = search_by_name(name)
        if element:
            display_element(element)
        else:
            print(f"No element found with name '{name}'.")

    elif choice == "4":
        print(f"\n{'No.':<5} {'Symbol':<8} {'Name':<15} {'Mass (u)':<12} {'Density'}")
        print("-" * 55)
        for element in periodictable.elements:
            if element.symbol:
                density = f"{element.density} g/cm³" if element.density else "N/A"
                print(f"{element.number:<5} {element.symbol:<8} {element.name.capitalize():<15} {element.mass:<12} {density}")
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
