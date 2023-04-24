import json
import sys

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments. Please run the program with 'python3 gen_webhooks.py webhooks.json'")

    webhooks_file = open("webhooks.json")
    webhooks_data = json.load(webhooks_file)

    discohook_file = open("discohook.json")
    discohook_data = json.load(discohook_file)

    for boss in webhooks_data:
        webhook = webhooks_data[boss]['webhook']
        thread_id = webhooks_data[boss]['thread_id']
        discohook = discohook_data[boss]['discohook']
        print(f'{boss}\n{discohook}\n{webhook}?thread_id={thread_id}\n')

if __name__ == "__main__":
    main()