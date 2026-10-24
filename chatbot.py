
print("🥗 Welcome to NutriBot!")
print("Your Personal Nutrition Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("NutriBot: Goodbye! Stay healthy! 😊")
        break

    elif "hello" in user or "hi" in user:
        print("NutriBot: Hello! How can I help you with nutrition?")

    elif "protein" in user:
        print("NutriBot: Eggs, milk, beans, nuts, and lentils are good sources of protein.")

    elif "fruit" in user:
        print("NutriBot: Apples, bananas, oranges, and berries are healthy fruits.")

    elif "vegetable" in user:
        print("NutriBot: Spinach, carrots, broccoli, and tomatoes are nutritious vegetables.")

    elif "water" in user:
        print("NutriBot: Drink water regularly throughout the day.")

    elif "weight loss" in user:
        print("NutriBot: Eat balanced meals, stay active, and get enough sleep.")

    elif "healthy food" in user:
        print("NutriBot: Eat fruits, vegetables, whole grains, and protein-rich foods.")

    elif "vitamin" in user:
        print("NutriBot: Fruits and vegetables provide many important vitamins.")
    elif "breakfast" in user:
    print("NutriBot: Eat a healthy breakfast like oats, eggs, fruits, or idli to start your day!")
    else:
        print("NutriBot: Sorry, I don't know that yet. Ask me about healthy food!")
        
