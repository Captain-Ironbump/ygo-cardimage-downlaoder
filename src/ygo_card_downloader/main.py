# Eingabeparameter
# 1: csv oder json datei mit id's
# 2: Destination-Ordner
# 3: api-endpint (Wahl zwichen 'cards'|'cards_small'|'cards_cropped')

import argparse
import json
from ygo_card_downloader.config import Config
from ygo_card_downloader.api_client import ApiClient
from ygo_card_downloader.validator import validate_input, validate_output


def main():
    parser = argparse.ArgumentParser(
        description="YGOPro Card images Download Script from the official YGOPro API"
    )
    parser.add_argument("ids", help="CSV or JSON file containing the IDs")
    parser.add_argument("destination", help="Destination Folder")
    parser.add_argument(
        "-e",
        "--api-endpoint",
        default="cards",
        choices=["cards", "cards_small", "cards_cropped"],
        help="API endpoint to use (default: cards)",
    )
    args = parser.parse_args()

    input_file = validate_input(args.ids)
    output_folder = validate_output(args.destination)

    config = Config()
    api_client = ApiClient(config=config)

    cards = []
    with open(input_file, "r", encoding="utf-8") as file:
        cards = json.load(file)

    if cards is None or len(cards) == 0:
        raise ValueError("No cards to download")

    # print(cards)

    print("Downloading images")
    api_client.download_images(args.api_endpoint, output_folder, cards)
    print("Done")


if __name__ == "__main__":
    main()
