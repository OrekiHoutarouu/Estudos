import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    str = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            str.append(row)

    dna = []
    with open(sys.argv[2], "r") as file:
        reader = file

        for row in reader:
            dna = row[:-1]

    longestAGATC = longest_match(dna, "AGATC")
    longestAATG = longest_match(dna, "AATG")
    longestTATC = longest_match(dna, "TATC")

    if sys.argv[1] == "databases/large.csv":
        longestTTTTTTCT = longest_match(dna, "TTTTTTCT")
        longestTCTAG = longest_match(dna, "TCTAG")
        longestGATA = longest_match(dna, "GATA")
        longestGAAA = longest_match(dna, "GAAA")
        longestTCTG = longest_match(dna, "TCTG")

    for person in str:
        if sys.argv[1] == "databases/small.csv":
            if (
                int(person["AGATC"]) == longestAGATC
                and int(person["AATG"]) == longestAATG
                and int(person["TATC"]) == longestTATC
            ):
                print(person["name"])
                return
        else:
            if (
                int(person["AGATC"]) == longestAGATC
                and int(person["AATG"]) == longestAATG
                and int(person["TATC"]) == longestTATC
                and int(person["TTTTTTCT"]) == longestTTTTTTCT
                and int(person["TCTAG"]) == longestTCTAG
                and int(person["GATA"]) == longestGATA
                and int(person["GAAA"]) == longestGAAA
                and int(person["TCTG"]) == longestTCTG
            ):
                print(person["name"])
                return

    print("No match")


def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1

            else:
                break

        longest_run = max(longest_run, count)

    return longest_run

if __name__ == "__main__":
    main()
