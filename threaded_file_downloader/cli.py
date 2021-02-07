"""Console script for threaded_file_downloader."""
import argparse
import sys
import threading
import requests


def main():
    """Console script for threaded_file_downloader."""
    parser = argparse.ArgumentParser()

    parser = argparse.ArgumentParser(description="Request urls and save contents")

    parser.add_argument(
        "infile",
        type=argparse.FileType("r"),
        help="Input file containing urls seperated by newline",
    )

    parser.add_argument(
        "outdir",
        type=str,
        help="Output directory",
    )

    args = parser.parse_args()

    urls = [x for x in args.infile.readlines() if x != ""]

    def download(url: str):
        bytes_: bytes = requests.get(url).content

        filename = url.rsplit("/", 1)[1]

        f = open(filename, "wb")
        f.write(bytes_)
        f.close()

    for url in urls:

        x = threading.Thread(target=download, args=(url.strip("\n"),))
        x.start()

        print("Arguments: " + str(args._))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
