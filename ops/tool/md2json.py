#!/usr/local/bin python3

import json
import argparse
import re
import os


def analyst(md, author_id):
    tag_pattern = re.compile(r'\[//\]: \<\> \((.*?)\)')
    with open(md, "r") as fp:
        lines = fp.readlines()
        if not lines:
            return None
        title = lines[0].strip("# \n")
        content = "".join(lines)
        tags = []
        for i in range(1, 3):
            res = tag_pattern.match(lines[i])
            if res:
                tags = [s.strip() for s in res.group(1).split(",")]
                break
        return {
            "title": title,
            "content": content,
            "authorID": author_id,
            "tags": tags
        }


def main():
    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=200),
                                     description="""example:
      python3 md2json.py -a author-id --article "linux/centos8-vc66-安装.md"
      python3 md2json.py -a author-id -d "linux,golang"
    """)
    parser.add_argument("-a", "--author-id", help="author id")
    parser.add_argument("--article", help="article")
    parser.add_argument("-d", "--directory", help="directory")
    args = parser.parse_args()

    if args.article:
        print(json.dumps(analyst(args.article, args.author_id)))
        return
    if args.directory:
        for d in args.directory.split(","):
            filenames = [os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and f.endswith(".md") and f != "README.md"]
            for filename in filenames:
                print(json.dumps(analyst(filename, args.author_id)))


if __name__ == '__main__':
    main()
