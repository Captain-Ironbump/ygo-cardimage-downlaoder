# Eingabeparameter
# 1: csv oder json datei mit id's
# 2: Destination-Ordner
# 3: api-endpint (Wahl zwichen 'cards'|'cards_small'|'cards_cropped')

import argparse
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

    print(input_file, output_folder, args.api_endpoint)


if __name__ == "__main__":
    main()
