import csv
from pathlib import Path

INPUT_FILE = Path("input.csv")
OUTPUT_FILE = Path("follow_up.csv")


def main():
    if not INPUT_FILE.exists():
        print(f"エラー: {INPUT_FILE} が見つかりません")
        return

    follow_up_rows = []

    with INPUT_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["対応状況"].strip() == "未対応":
                follow_up_rows.append(row)

    with OUTPUT_FILE.open("w", encoding="utf-8-sig", newline="") as file:
        fieldnames = ["会社名", "担当者", "メール", "対応状況"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(follow_up_rows)

    print(f"完了: 未対応の{len(follow_up_rows)}件を {OUTPUT_FILE} に出力しました")


if __name__ == "__main__":
    main()