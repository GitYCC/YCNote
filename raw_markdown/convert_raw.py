import re
import shutil
import argparse

from pathlib2 import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / 'raw_markdown' / 'content'
CONVERT_ROOT = ROOT / 'content'
CATEGORIES = dict(ai_ml='AI_ML', coding='Coding', life='Life', reading='Reading')
WEB_MEDIA_FMT = 'http://www.ycc.idv.tw/media/{}'


def change_content(content, convert_asset_folder):
    pattern = r'!\[(.*)\]\(.?\/?asset\/(.*)\)'
    replaced = '![\\1]({}/\\2)'.format(WEB_MEDIA_FMT.format(convert_asset_folder.name))
    return re.sub(pattern, replaced, content)


def parse_args():
    parser = argparse.ArgumentParser(description='Convert raw markdown files.')
    parser.add_argument('--name', metavar='name', type=str, nargs=1,
                        help='name of the folder in content/')
    args = parser.parse_args()
    return args


def main(name):
    raw_folder = RAW_ROOT / name
    raw_md_list = [child for child in raw_folder.glob('*.md')]
    raw_asset = raw_folder / 'asset'

    convert_asset_folder = CONVERT_ROOT / 'media' / name

    shutil.rmtree(str(convert_asset_folder))
    shutil.copytree(str(raw_asset), str(convert_asset_folder))

    for raw_md in raw_md_list:
        content = raw_md.read_text()
        match = re.search(r'Category:\ *(.+)\n', content)
        if not match:
            continue
        category = match.group(1).replace('.', '_').lower()
        content = change_content(content, convert_asset_folder)
        convert_md_folder = CONVERT_ROOT / 'articles' / category
        new_md = convert_md_folder / raw_md.name
        new_md.write_text(content)


if __name__ == '__main__':
    args = parse_args()
    name = args.name[0]
    main(name)
