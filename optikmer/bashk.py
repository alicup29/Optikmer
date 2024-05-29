import argparse
from pathlib import Path

def add_args(parser):
    """
    CHANGE LATER
    Add command line arguments to the parser.

    Args:
    - parser (argparse.ArgumentParser): Argument parser object.

    Returns:
    - argparse.ArgumentParser: Parser with added arguments.
    """

    parser.add_argument(
        "--kmer-lengths",
        type=int,
        default=[],
        nargs='+',
        help="",
    )

    parser.add_argument(
        "--show-hist",
        action="store_true",
        help="",
    )

    parser.add_argument(
        "-f",
        "--fastq",
        type=Path,
        help="",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path.cwd(),
        help="",
    )

def main(args):
    print("Passed args")
    print("kmer lengths: ",args.kmer_lengths)
    print("Show Hist: ",args.show_hist)
    print("Input fastq: ",args.fastq)
    print("Output path: ",args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    args = add_args(parser).parse_args()

    if args.fastq is None:
        parser.error(
            "A valid fastq file must be given. See optikmer --help for more information"
        )

    main(args)