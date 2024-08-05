from pathlib import Path

PROJ = Path(__file__).parent

CH01 = PROJ / "ch01"
CH02 = PROJ / "ch02"
CH03 = PROJ / "ch03"
CH04 = PROJ / "ch04"
CH05 = PROJ / "ch05"

if __name__ == "__main__":
    print(PROJ)