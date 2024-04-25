from tabulate import tabulate

def main():
    print("\nTV-Show Manager")
    watchlist, count = [], 0

    while True:
        action = get_input()

        if action == "V":
            view(watchlist)
        elif action == "A":
            watchlist, count = create(watchlist, count)
        elif action == "U":
            watchlist = update(watchlist)
        elif action == "D":
            watchlist = delete(watchlist)
        else:
            break

def get_input():
    instructions = [{"Key": "V", "Action": "View TV-Shows"},
                    {"Key": "A", "Action": "Add a Show to Watchlist"},
                    {"Key": "U", "Action": "Update Show Status"},
                    {"Key": "D", "Action": "Delete a Show"},
                    {"Key": "E", "Action": "Exit"}]

    while True:
        print(tabulate(instructions, headers="keys", tablefmt="rounded_outline"))
        action = input("What do you want to do?: ").upper()

        if action in ["V", "A", "U", "D", "E"]:
            return action
        else:
            print("Invalid key, try again.")

def view(watchlist):
    print("\nWatchlist:")
    print(tabulate(watchlist, headers="keys", tablefmt="rounded_grid"))

def create(data, i):
    show, i = input("Show: "), i + 1
    data.append({"ID": i, "Show": show, "Status": "Watchlist"})
    return data, i

def update(watchlist):
    show_id = int(input("Enter the ID of the show to update: "))
    for data in [watchlist]:
        for show in data:
            if show["ID"] == show_id:
                new_status = input("Enter updated status (Watchlist, Watching, Finished): ").capitalize()
                show["Status"] = new_status
    return watchlist



def delete(data):
    show_id = int(input("Enter the ID of the show to delete: "))
    for show in data:
        if show["ID"] == show_id:
            data.remove(show)
            return data

    print("Invalid show ID.")
    return data

if __name__ == "__main__":
    main()
