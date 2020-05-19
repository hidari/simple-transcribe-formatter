import argparse
import json

description = """
This program takes JSON data from Amazon Transcribe and formats it into a conversational format.
"""

parser = argparse.ArgumentParser(description=description)
parser.add_argument("-i", "--input", required=True, help="Input JSON file path")
parser.add_argument("-o", "--output", default="result.txt", help="output file path")


def load(path):
    with open(path) as f:
        raw = json.load(f)

    return raw


def format_from(raw_data):
    segments = raw_data["results"]["speaker_labels"]["segments"]
    items = raw_data["results"]["items"]

    speeches = []
    for segment in segments:
        speaker = segment["speaker_label"]
        separators = segment["items"]
        speech = f"{speaker}: "
        words = []
        for separator in separators:
            start = separator["start_time"]
            end = separator["end_time"]
            word = ""
            for item in items:
                if "start_time" not in item or "end_time" not in item:
                    continue
                if item["start_time"] == start and item["end_time"] == end:
                    word = item["alternatives"][0]["content"]
                    break

            words.append(word)
        speeches.append(speech + " ".join(words))

    return "\n".join(speeches)


def save(data, path):
    with open(path, mode="w") as output:
        output.write(data)

    return


if __name__ == "__main__":
    args = parser.parse_args()
    save(
        format_from(load(args.input)),
        args.output
    )
