import re
import shutil
import argparse

from PIL import Image
from pathlib2 import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / 'raw_markdown' / 'content'
CONVERT_ROOT = ROOT / 'content'
CATEGORIES = dict(ai_ml='AI_ML', coding='Coding', life='Life', reading='Reading')
WEB_MEDIA_FMT = 'http://www.ycc.idv.tw/media/{}'
WATERMARK_PATH = ROOT / 'raw_markdown' / 'logo.png'


def change_content(content, convert_asset_folder):
    pattern = r'!\[(.*)\]\(.?\/?asset\/(.*)\)'
    replaced = '![\\1]({}/\\2)'.format(WEB_MEDIA_FMT.format(convert_asset_folder.name))
    return re.sub(pattern, replaced, content)


def add_watermark(folder):
    watermark = Image.open(WATERMARK_PATH).convert('RGBA')
    watermark_width, watermark_height = watermark.size
    watermark_ratio = watermark_width / watermark_height

    for image_path in folder.glob('IMG_*'):
        try:
            main = Image.open(str(image_path))
        except IOError:
            continue

        main_width, main_height = main.size
        if main_width <= main_height:
            new_mark_height = main_height / 10.0
            new_mark_size = (new_mark_height * watermark_ratio, new_mark_height)
        else:
            new_mark_width = main_width / 13.0
            new_mark_size = (new_mark_width, new_mark_width / watermark_ratio)

        mark = watermark.copy()
        mark.thumbnail(new_mark_size, Image.ANTIALIAS)

        mark_width, mark_height = mark.size
        position = ((main_width - mark_width), (main_height - mark_height))
        main.paste(mark, position, mark)
        main.save(str(image_path), quality=95)


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

    if convert_asset_folder.exists():
        shutil.rmtree(str(convert_asset_folder))
    shutil.copytree(str(raw_asset), str(convert_asset_folder))
    add_watermark(convert_asset_folder)

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
