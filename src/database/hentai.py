from typing import Generator

from peewee import fn

from .models import Hentai
from .favorite import delete_hentai_from_favorites


def add_hentai(code: int | str, title: str, description: str, url: str, photo_id: str = None) -> int:
    try:
        new_hentai = Hentai(code=code, title=title, description=description, photo_id=photo_id, url=url)
        new_hentai.save()
        return new_hentai.id
    except Exception as e:
        print(e)


def get_hentai_by_code_or_none(code: int) -> dict[str, str, str, str] | None:
    hentai = Hentai.get_or_none(Hentai.code == code)

    return {
            'code': hentai.code,
            'title': hentai.title,
            'description': hentai.description,
            'photo': hentai.photo_id,
            'url': hentai.url
            } if hentai else None


def get_random_hentai_code():
    random_index = Hentai.select().order_by(fn.Random()).first().code
    return random_index


def get_fresh_hentai(count: int):
    yield from ((hentai.code, hentai.title) for hentai in Hentai.select().order_by(Hentai.id.desc()).limit(count))


def get_all_hentai() -> Generator:
    yield from ((hentai.code, hentai.title) for hentai in Hentai.select())


def delete_hentai_by_code(code: int) -> bool:
    try:
        delete_hentai_from_favorites(code)
        Hentai.get_or_none(Hentai.code == code).delete_instance()
    except AttributeError:
        return False
    else:
        return True
