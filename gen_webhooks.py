import json
import sys

def main():

    if len(sys.argv) != 2:
        print("Invalid number of arguments. Please run the program with 'python3 gen_webhooks.py webhooks.json'")
        return

    webhooks_file_path = sys.argv[1]
    with open(webhooks_file_path) as webhooks_file:
        webhooks_data = json.load(webhooks_file)

    with open("discohook.json") as discohook_file:
        discohook_data = json.load(discohook_file)

    for boss in webhooks_data:
        webhook = webhooks_data[boss]['webhook']
        thread_id = webhooks_data[boss]['thread_id']
        discohook = discohook_data[boss]
        print(f'{boss}\n{discohook}\n{webhook}?thread_id={thread_id}\n')

if __name__ == "__main__":
    main()