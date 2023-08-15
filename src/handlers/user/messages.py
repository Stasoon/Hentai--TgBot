import random


class Messages:
    @staticmethod
    def get_welcome(user_name: str = 'незнакомец') -> str:
        return f'''👋 <b>Привет, {user_name}!</b> \n
🔎 Я выдаю название Хентая по коду из Telegram, TikTok, YouTube, Instagram \n
👇 Жми на кнопку ниже'''

    @staticmethod
    def get_menu():
        return '❓ Что вы хотите сделать?'

    @staticmethod
    def get_search() -> str:
        emojis = [emoji for emoji in '🍓🔞🔥💢📛']
        return f'{random.choice(emojis)} Введите код хентая:'

    @staticmethod
    def get_not_sub() -> str:
        return f"""Чтобы начать пользоваться ботом, подпишитесь на следующие каналы:"""

    @staticmethod
    def get_formatted_hentai_description(title: str, description: str = 'Упс, какая-то ошибка 😓') -> str:
        return f"<b><i>{title}</i></b> \n\n▸ <b>Описание:</b> {description}"

    @staticmethod
    def get_hentai_not_found(code: int) -> str:
        return f'Хентай с кодом «<code>{code}</code>» не найден 😓 \n\nПопробуйте позже, он скоро будет добавлен 👀'

    @staticmethod
    def get_code_incorrect():
        return '😓 Вы ввели не число. Попробуйте снова:'

    @staticmethod
    def get_unexpected():
        return '🔲 Пожалуйста, пользуйтесь клавиатурой'

    @staticmethod
    def get_fresh():
        return '🔥 Вот, что удалось найти среди новинок:'

    @staticmethod
    def get_favorite():
        return '⭐ Вот ваши избранные:'

    @staticmethod
    def get_favorite_empty():
        return '⭐ Ваше избранное пока пусто'
