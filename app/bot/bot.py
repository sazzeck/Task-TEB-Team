from typing import Tuple
from asgiref.sync import sync_to_async

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ParseMode
import aiogram.utils.markdown as md

from main.models import User
from django.contrib.auth.hashers import make_password

from data import AirtableUsers

from utils import Config


class MyBot:
    storage = MemoryStorage()

    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher(bot=bot, storage=storage)

    Bot.set_current(bot)
    Dispatcher.set_current(dp)

    @classmethod
    def register_handler(cls):
        cls.dp.register_message_handler(cmd_start, commands=["start"])
        cls.dp.register_message_handler(registration, state=Form.password)

    @classmethod
    def run(cls):
        cls.register_handler()
        executor.start_polling(
            cls.dp,
            on_startup=cls.on_startup,
            on_shutdown=cls.on_shutdown,
            skip_updates=True,
        )

    @staticmethod
    async def on_startup(dp: Dispatcher):
        pass

    @staticmethod
    async def on_shutdown(dp: Dispatcher):
        pass


@sync_to_async
def add_user(user_id: int, username: str, password: str) -> Tuple[User, bool]:
    return User.objects.get_or_create(
        id=user_id,
        defaults={
            "username": username,
            "password": password,
        },
    )


class Form(StatesGroup):
    username = State()
    password = State()


markup = ReplyKeyboardRemove()
user_table = AirtableUsers()


async def cmd_start(message: Message):
    await message.reply(
        md.text(
            md.text(md.bold("Registration")),
            md.text("Username is set automatically."),
            sep="\n",
        ),
        reply_markup=markup,
        parse_mode=ParseMode.MARKDOWN,
    )
    await Form.password.set()
    await message.answer(
        md.text(md.bold("Enter password")),
        reply_markup=markup,
        parse_mode=ParseMode.MARKDOWN,
    ),


async def registration(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["username"] = message.from_user.username
        data["password"] = message.text
        if not user_table.user_is_created(message.from_user.id):
            user, _ = await add_user(
                user_id=message.from_user.id,
                username=message.from_user.username,
                password=make_password(data["password"]),
            )
            user_table.user_create(
                tg_id=message.from_user.id,
                username=message.from_user.username,
                firstname=message.from_user.first_name,
                password=make_password(data["password"]),
            )
            await message.answer(
                md.text(
                    md.text(md.bold("Registration Completed")),
                    md.text(md.bold("Username: "), data["username"]),
                    md.text(md.bold("Password: "), data["password"]),
                    sep="\n",
                ),
                reply_markup=markup,
                parse_mode=ParseMode.MARKDOWN,
            )
        else:
            await message.answer(
                md.text(
                    md.text(
                        f"{md.bold(message.from_user.username)}, you have already registered."
                    ),
                ),
                reply_markup=markup,
                parse_mode=ParseMode.MARKDOWN,
            )

    await state.finish()
