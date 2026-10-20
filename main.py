from pathlib import Path


def analyze_log(file_path):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    total_entries = 0

    with open(file_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            line = line.strip()
            if not line:
                continue

            total_entries += 1
            level = line.split(":", 1)[0].upper()

            if level in counts:
                counts[level] += 1

    return counts, total_entries


def main():
    log_path = Path(__file__).with_name("sample.log")

    try:
        counts, total = analyze_log(log_path)
    except FileNotFoundError:
        print("Error: sample.log was not found.")
        return

    print("===== PyLogCheck Report =====")
    print()
    for level, count in counts.items():
        print(f"{level}: {count}")
    print()
    print(f"Total log entries: {total}")


if __name__ == "__main__":
    main()
