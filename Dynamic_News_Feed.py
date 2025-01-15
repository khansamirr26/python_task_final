news_feed = []

def add_news():
    print("\n--- Add News ---")
    title = input("Enter News Title: ")
    description = input("Enter News Details: ")
    photo_path = input("Enter Photo Path or URL: ")

    news_feed.append({
        "title": title,
        "description": description,
        "photo_path": photo_path
    })
    print("\nNews added successfully!\n")

def list_news():
    if not news_feed:
        print("\nNo news available.\n")
        return

    print("\n--- News List ---")
    for i, news in enumerate(news_feed, start=1):
        print(f"{i}. Title: {news['title']}")
        print(f"   Details: {news['description']}")
        print(f"   Photo: {news['photo_path']}\n")

def main():
    while True:
        print("\n--- News Feed Application ---")
        print("1. Add News Details")
        print("2. List News")
        print("3. Exit App")

        choice = input("Select your choice: ")

        if choice == "1":
            add_news()
        elif choice == "2":
            list_news()
        elif choice == "3":
            print("\nExiting the application. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.\n")

if __name__ == "__main__":
    main()