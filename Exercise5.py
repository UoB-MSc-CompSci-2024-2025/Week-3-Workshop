temperature = int(input("What will the temperature be tomorrow? "))
rain = bool(input("Will it rain tomorrow? "))

if temperature > 20:
    outfit = "shorts and a t-shirt" if not rain else "warm clothing but be prepared for rain"
elif temperature >= 10:
    outfit = "trousers and a jumper" if not rain else "something warm and bring an umbrella"
else:
    outfit = "a warm coat" if not rain else "a warm coat and an umbrella"

print(f"Wear {outfit}")