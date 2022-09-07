import requests
import csv
from typing import List


GLOBAL_TEMP_INDEX_URL = (
    "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
)

metadata_offset = 1
missing_character = "***"
alternative_character = "NA"
r = requests.get(GLOBAL_TEMP_INDEX_URL)


def split_clean_line(line: str) -> List[str]:
    return [
        s.replace(missing_character, alternative_character) for s in line.split(",")
    ]


with open("data/test.csv", "w") as f:
    writer = csv.writer(f)
    lines = [split_clean_line(s) for s in r.text.splitlines()[metadata_offset:]]
    writer.writerows(lines)


if __name__ == "__main__":
    # status
    print(r.status_code)
    # metadata
    print(r.text.splitlines()[0 : metadata_offset - 1])
    # number of records
    print(len(r.text.splitlines()[metadata_offset:]))
    # actual data
    # print(r.text)
