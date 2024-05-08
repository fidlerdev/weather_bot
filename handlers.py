from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import get_kb_text
from keyboard import get_keyboard
from weather import get_weather_by_city, get_weather_by_location

router = Router()

class BotStates(StatesGroup):
    # Получаем погоду по городу
    wbcity = State()

@router.message(Command("start"))
async def start_command(message: types.Message) -> None:
    await message.answer(
        "Привет! Я помогу тебе узнать погоду в любом городе мира!",
        reply_markup=get_keyboard()
    )

@router.message(F.location)
async def process_location_weather(message: types.Message) -> None:
    if not message.location:
        await message.reply("Ошибка!")
        return

    temperature = get_weather_by_location(
                                            message.location.latitude,
                                            message.location.longitude
                                            )

    await message.answer(f"Температура в вашем городе — {temperature} °C")

@router.message(F.text == get_kb_text().weather_by_city)
async def input_city_name(message: types.Message, state: FSMContext) -> None:
    await state.set_state(BotStates.wbcity)
    await message.answer("Введите название города")

@router.message(BotStates.wbcity)
async def process_city_weather(message: types.Message, state: FSMContext) -> None:
    city_name = message.text or ""
    temperature = await get_weather_by_city(city_name)
    await message.answer(f"Температура в городе \"{city_name}\" — {temperature} °C")
    await state.set_data({"Print": "ok"})
    print(await state.get_data())

    await state.set_data({"Print@!": "not  ok"})
    print(await state.get_data())
    await state.set_data({"Print": "ok"})
    await state.clear()