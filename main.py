import argparse


if __name__=="__main__":
    parser = argparse.ArgumentParser(
        prog="Advent of Code",
        description="Runs Ollie's suite of advent of code solutions",
    )

    parser.add_argument('-y', '--year', type=int, default=2022, choices=range(2015, 2022))
    parser.add_argument('-d', '--day',  required=True, type=int, choices=range(1, 25))
    parser.add_argument('-s', '--step', type=int, default=1, choices=range(1,2))
    parser.add_argument('-i', '--input', type=str)

    inp