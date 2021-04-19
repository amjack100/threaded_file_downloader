"""Console script for threaded_file_downloader."""
import sys
import threading
import requests
import click
import os

def download(url: str, outdir):

    bytes_: bytes = requests.get(url).content

    filename = url.rsplit("/", 1)[1]

    outfile = os.path.join(outdir, filename)
    
    with open(outfile, 'wb') as f:
        f.write(bytes_)


@click.command(help="Download a list of urls from a text file (seperated by line)")
@click.argument('input-file')
@click.argument('output-dir')
def main(input_file, output_dir):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(input_file) as f:
        
        for line in f.readlines():
            if line != "":
                x = threading.Thread(target=download, args=(line.strip("\n"), output_dir))
                x.start()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
