#!/usr/bin/env python3
import sys

from page_loader.cli import get_args
from page_loader.main import download


def main():
    """
    Entry point

    :return:
    """
    args = get_args()

    try:
        result = download(url=args.url, out_dir=args.output)
        print(f"Page was downloaded as {result}")
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
