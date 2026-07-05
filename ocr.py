import cv2
import pytesseract
import re

from config import TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def extract_trip(text):
    matches = re.findall(r'(\d+(?:\.\d+)?)\s*km', text.lower())

    if len(matches) > 0:
        return float(matches[-1])

    return None


def extract_data(image_path):

    image = cv2.imread(image_path)

    text = pytesseract.image_to_string(image)
    text = text.replace(",", ".")

    # Fare like $5 or $5.50
    fare_match = re.search(r"\$(\d+(?:\.\d+)?)", text)

    # Distances like 2.5km or ~2.5km
    distance_matches = re.findall(r"~?\s*(\d+(?:\.\d+)?)\s*km", text, re.IGNORECASE)

    fare = float(fare_match.group(1)) if fare_match else None

    pickup = float(distance_matches[0]) if len(distance_matches) >= 1 else None

    trip = extract_trip(text)

    return {
        "fare": fare,
        "pickup": pickup,
        "trip": trip,
        "raw_text": text
    }