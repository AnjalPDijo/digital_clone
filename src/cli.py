import argparse
from main import DigitalClone

def main():
    parser = argparse.ArgumentParser(description='Interact with your Digital Clone.')
    parser.add_argument('action', choices=['add_like', 'add_dislike', 'set_behavior', 'remove_like', 'remove_dislike', 'remove_behavior', 'update_like', 'update_dislike', 'update_behavior', 'list'], help='Action to perform')
    parser.add_argument('--item', help='Item for like/dislike')
    parser.add_argument('--behavior', help='Behavior to set/update')
    parser.add_argument('--description', help='Description for behavior')
    parser.add_argument('--new_item', help='New item for update')
    args = parser.parse_args()

    clone = DigitalClone()

    if args.action == 'add_like':
        clone.add_like(args.item)
        print(f"Added like: {args.item}")
    elif args.action == 'add_dislike':
        clone.add_dislike(args.item)
        print(f"Added dislike: {args.item}")
    elif args.action == 'set_behavior':
        clone.set_behavior(args.behavior, args.description)
        print(f"Set behavior: {args.behavior} -> {args.description}")
    elif args.action == 'remove_like':
        clone.remove_like(args.item)
        print(f"Removed like: {args.item}")
    elif args.action == 'remove_dislike':
        clone.remove_dislike(args.item)
        print(f"Removed dislike: {args.item}")
    elif args.action == 'remove_behavior':
        clone.remove_behavior(args.behavior)
        print(f"Removed behavior: {args.behavior}")
    elif args.action == 'update_like':
        clone.update_like(args.item, args.new_item)
        print(f"Updated like: {args.item} -> {args.new_item}")
    elif args.action == 'update_dislike':
        clone.update_dislike(args.item, args.new_item)
        print(f"Updated dislike: {args.item} -> {args.new_item}")
    elif args.action == 'update_behavior':
        clone.update_behavior(args.behavior, args.description)
        print(f"Updated behavior: {args.behavior} -> {args.description}")
    elif args.action == 'list':
        data = clone.get_data()
        print("Likes:", data['likes'])
        print("Dislikes:", data['dislikes'])
        print("Behaviors:", data['behaviors'])

if __name__ == "__main__":
    main()
