import json

with open("knowledge_base.json", "r") as file:
    destinations = json.load(file)

print("=" * 50)
print("AI TRAVEL PLANNER")
print("=" * 50)

destination = input("Enter destination (Goa/Jaipur/Kerala): ")

if destination in destinations:

    data = destinations[destination]

    print("\nDestination:", destination)
    print("Recommended Days:", data["days"])
    print("Estimated Budget: ₹", data["budget"])

    print("\nPlaces to Visit:")
    for place in data["places"]:
        print("-", place)

    print("\nFood Recommendations:")
    for food in data["food"]:
        print("-", food)

    print("\nSuggested Itinerary")

    for i, place in enumerate(data["places"], start=1):
        print(f"Day {i}: Visit {place}")

else:
    print("Destination not found in knowledge base.")