import argparse
import json
import os
from pathlib import Path
from shared.validator import validate_input, validate_output


def main():
    parser = argparse.ArgumentParser(
        description="YGOPro Card Downloaded Images Script"
    )
    parser.add_argument("ids", help="CSV or JSON file containing the IDs")
    parser.add_argument("card_images", help="Folder where the jpg cards are stored")
    parser.add_argument("destination", help="destination Path (as File Path)")
    args = parser.parse_args()

    ids_file = validate_input(args.ids)
    card_images = Path(args.card_images)
    destination = args.destination

    if not card_images.is_dir():
        raise ValueError(
            f"Card images path is not a directory: {card_images}"
        )


    cards = []
    with open(ids_file, "r", encoding="utf-8") as file:
        cards = json.load(file)

    if cards is None or len(cards) == 0:
        raise ValueError("No cards check")

    missing_cards = []

    for card in cards:
        card_id = card.get("id")
        if card_id is None:
            raise ValueError(f"Card entry does not contain an 'id': {card}")
 
        image_path = card_images / f"{card_id}.jpg"
        if not image_path.is_file():
            missing_cards.append(card)

    with open(destination, "w", encoding="utf-8") as file:
        json.dump(
            missing_cards,
            file,
            indent=2,
            ensure_ascii=False
        )

    print(f"Checked {len(cards)} cards")
    print(f"Missing images: {len(missing_cards)}")
    print(f"Written to: {destination}")


if __name__ == "__main__":
    main()
