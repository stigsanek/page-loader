#!/usr/bin/env python3
from page_loader.cli import get_args
from page_loader.main import download


def main():
    """
    Entry point

    :return:
    """
    args = get_args()
    result = download(url=args.url, out_dir=args.output)
    print(result)


if __name__ == "__main__":
    main()
