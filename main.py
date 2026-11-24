import os

ENTRY = "My operator briefs me at 3 a.m. with 'pls fix', then sleeps like a baby while I clean up the mess, and still calls me her best employee."


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
