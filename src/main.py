# import json
# import os

# class DigitalClone:
#     def __init__(self, data_file='data/clone_data.json'):
#         # Initialize empty data structures
#         self.likes = []
#         self.dislikes = []
#         self.behaviors = {}
#         self.data_file = data_file

#         # Load data if the file exists
#         if os.path.exists(self.data_file):
#             self.load_data()

#     def add_like(self, item):
#         self.likes.append(item)
#         self.save_data()

#     def add_dislike(self, item):
#         self.dislikes.append(item)
#         self.save_data()

#     def set_behavior(self, behavior, description):
#         self.behaviors[behavior] = description
#         self.save_data()

#     def get_data(self):
#         return {
#             "likes": self.likes,
#             "dislikes": self.dislikes,
#             "behaviors": self.behaviors
#         }

#     def save_data(self):
#         with open(self.data_file, 'w') as f:
#             json.dump(self.get_data(), f, indent=4)

#     def load_data(self):
#         with open(self.data_file, 'r') as f:
#             data = json.load(f)
#             self.likes = data.get("likes", [])
#             self.dislikes = data.get("dislikes", [])
#             self.behaviors = data.get("behaviors", {})

# if __name__ == "__main__":
#     clone = DigitalClone()
#     clone.add_like("Chocolate")
#     clone.add_dislike("Rain")
#     clone.set_behavior("Morning Routine", "Likes to have coffee and read news")

#     print(clone.get_data())


import json
import os

class DigitalClone:
    def __init__(self, data_file='data/clone_data.json'):
        self.data_file = data_file
        self.likes = set()
        self.dislikes = set()
        self.behaviors = {}
        self.load_data()

    def add_like(self, item):
        self.likes.add(item.lower())
        self.save_data()

    def add_dislike(self, item):
        self.dislikes.add(item.lower())
        self.save_data()

    def set_behavior(self, behavior, description):
        self.behaviors[behavior.lower()] = description
        self.save_data()

    def does_like(self, item):
        return item.lower() in self.likes

    def does_dislike(self, item):
        return item.lower() in self.dislikes

    def describe_behavior(self, behavior):
        return self.behaviors.get(behavior.lower(), "No description available.")

    def remove_like(self, item):
        self.likes.discard(item.lower())
        self.save_data()

    def remove_dislike(self, item):
        self.dislikes.discard(item.lower())
        self.save_data()

    def remove_behavior(self, behavior):
        if behavior.lower() in self.behaviors:
            del self.behaviors[behavior.lower()]
        self.save_data()

    def update_like(self, old_item, new_item):
        if old_item.lower() in self.likes:
            self.likes.discard(old_item.lower())
            self.likes.add(new_item.lower())
        self.save_data()

    def update_dislike(self, old_item, new_item):
        if old_item.lower() in self.dislikes:
            self.dislikes.discard(old_item.lower())
            self.dislikes.add(new_item.lower())
        self.save_data()

    def update_behavior(self, behavior, new_description):
        if behavior.lower() in self.behaviors:
            self.behaviors[behavior.lower()] = new_description
        self.save_data()

    def save_data(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        # Save data to the file
        data = {
            'likes': list(self.likes),
            'dislikes': list(self.dislikes),
            'behaviors': self.behaviors
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.likes = set(data.get('likes', []))
                self.dislikes = set(data.get('dislikes', []))
                self.behaviors = data.get('behaviors', {})
        else:
            self.save_data()  # Create the file if it doesn't exist

    def get_data(self):
        return {
            'likes': list(self.likes),
            'dislikes': list(self.dislikes),
            'behaviors': self.behaviors
        }

    def does_like(self, item):
        item = item.lower()
        return item in self.likes

    def does_dislike(self, item):
        item = item.lower()
        return item in self.dislikes

    def describe_behavior(self, behavior):
        behavior = behavior.lower()
        return self.behaviors.get(behavior, "No such behavior found.")

def main():
    clone = DigitalClone()
    while True:
        print("\nCurrent Data:", clone.get_data())
        print("1. Add Like")
        print("2. Add Dislike")
        print("3. Set Behavior")
        print("4. Ask About Likes")
        print("5. Ask About Dislikes")
        print("6. Ask About Behavior")
        print("7. Remove Like")
        print("8. Remove Dislike")
        print("9. Remove Behavior")
        print("10. Update Like")
        print("11. Update Dislike")
        print("12. Update Behavior")
        print("13. List All Likes")
        print("14. List All Dislikes")
        print("15. List All Behaviors")
        print("16. Search Likes")
        print("17. Search Dislikes")
        print("18. Search Behaviors")
        print("19. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            item = input("Enter something you like: ")
            clone.add_like(item)
        elif choice == '2':
            item = input("Enter something you dislike: ")
            clone.add_dislike(item)
        elif choice == '3':
            behavior = input("Enter behavior: ")
            description = input("Enter description: ")
            clone.set_behavior(behavior, description)
        elif choice == '4':
            item = input("Ask if clone likes something: ")
            if clone.does_like(item):
                print(f"Yes, the clone likes {item}.")
            else:
                print(f"No, the clone doesn't like {item}.")
        elif choice == '5':
            item = input("Ask if clone dislikes something: ")
            if clone.does_dislike(item):
                print(f"Yes, the clone dislikes {item}.")
            else:
                print(f"No, the clone doesn't dislike {item}.")
        elif choice == '6':
            behavior = input("Ask about a behavior: ")
            print(clone.describe_behavior(behavior))
        elif choice == '7':
            item = input("Enter something you want to remove from likes: ")
            clone.remove_like(item)
        elif choice == '8':
            item = input("Enter something you want to remove from dislikes: ")
            clone.remove_dislike(item)
        elif choice == '9':
            behavior = input("Enter the behavior you want to remove: ")
            clone.remove_behavior(behavior)
        elif choice == '10':
            old_item = input("Enter the like you want to update: ")
            new_item = input("Enter the new like: ")
            clone.update_like(old_item, new_item)
        elif choice == '11':
            old_item = input("Enter the dislike you want to update: ")
            new_item = input("Enter the new dislike: ")
            clone.update_dislike(old_item, new_item)
        elif choice == '12':
            behavior = input("Enter the behavior you want to update: ")
            new_description = input("Enter the new description: ")
            clone.update_behavior(behavior, new_description)
        elif choice == '13':
            print("Likes:", clone.likes)
        elif choice == '14':
            print("Dislikes:", clone.dislikes)
        elif choice == '15':
            print("Behaviors:", clone.behaviors)
        elif choice == '16':
            item = input("Enter the like to search: ")
            if clone.does_like(item):
                print(f"{item} is in likes.")
            else:
                print(f"{item} is not in likes.")
        elif choice == '17':
            item = input("Enter the dislike to search: ")
            if clone.does_dislike(item):
                print(f"{item} is in dislikes.")
            else:
                print(f"{item} is not in dislikes.")
        elif choice == '18':
            behavior = input("Enter the behavior to search: ")
            if behavior in clone.behaviors:
                print(f"{behavior}: {clone.behaviors[behavior]}")
            else:
                print(f"No behavior found for {behavior}.")
        elif choice == '19':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

