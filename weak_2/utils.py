def get_valid_priority():
    while True:
        print("\nSelect Priority:")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            return "Low"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "High"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")