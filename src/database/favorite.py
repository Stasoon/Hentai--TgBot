from .models import Favorite, User, Hentai


def add_or_delete_favorite(user_id, hentai_code):
    user = User.get(User.telegram_id == user_id)
    hentai = Hentai.get(Hentai.code == hentai_code)

    favorite, created = Favorite.get_or_create(user=user, hentai=hentai)

    if not created:
        favorite.delete_instance()


def get_favorites_for_user(user_id: int):
    query = Favorite.select().join(User).where(User.telegram_id == user_id)
    return [(favorite.hentai.code, favorite.hentai.title) for favorite in query]


def is_hentai_in_favorites(user_id, hentai_code: int | str) -> bool:
    hentai_code = int(hentai_code)
    query = Favorite.select().join(User).where(User.telegram_id == user_id)

    for fav in query:
        if fav.hentai.code == hentai_code:
            return True
    return False


def delete_hentai_from_favorites(hentai_code: int):
    query = Favorite.select().join(Hentai).where(Hentai.code == hentai_code)
    for favorite in query:
        print(favorite.hentai.title, favorite.hentai.code)
        favorite.delete_instance()
