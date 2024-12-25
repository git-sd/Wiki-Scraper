import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_content(topic):
    link = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    print(f"Fetching content from: {link}")
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Page Title:", soup.title.text)
        return soup
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
        return None

initial_topic = input("Enter the Wikipedia topic name: ")

soup = fetch_wikipedia_content(initial_topic)

if soup:
    print("\nRelated topics (links) found on this page:")
    links = soup.find_all('a', href=True)
    related_topics = []
    for link in links:
        href = link['href']
        if href.startswith('/wiki/') and ':' not in href:
            related_topic = href.replace('/wiki/', '').replace('_', ' ')
            related_topics.append(related_topic)

    related_topics = list(set(related_topics))

    for i, topic in enumerate(related_topics, 1):
        print(f"{i}. {topic}")

    choice = int(input("\nEnter the number corresponding to your choice of topic: "))

    if 1 <= choice <= len(related_topics):
        selected_topic = related_topics[choice - 1]
        print(f"\nYou selected: {selected_topic}")
        fetch_wikipedia_content(selected_topic)
    else:
        print("Invalid choice.")
