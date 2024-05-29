import argparse
import pathlib
import optikmer.bashk

def main():
    parser = argparse.ArgumentParser(
        prog="Antidote",
        description="A Neural network Trained In Deleterious ObjecT Elimination",
    )

    modules = [optikmer.bashk]

    subparsers = parser.add_subparsers(title="Choose a command")
    subparsers.required = True

    def get_module_name(module):
        return pathlib.Path(module.__file__).stem

    for module in modules:
        this_parser = subparsers.add_parser(
            get_module_name(module), description=module.__doc__
        )
        module.add_args(this_parser)
        this_parser.set_defaults(func=module.main)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()