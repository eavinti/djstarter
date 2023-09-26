from enum import Enum


class Input(Enum):
    TEXT = "block px-4 w-full rounded-md border-0 py-1.5 bg-transparent text-black shadow-sm ring-1 ring-inset ring-black placeholder:text-black/10 focus:ring-2 focus:ring-inset focus:ring-bet-green sm:text-sm sm:leading-6"
    TEXT_LEFT = "block w-full rounded-md border-0 py-1.5 pl-10 pr-4 bg-transparent text-black ring-1 ring-inset ring-black placeholder:text-black/10 focus:ring-2 focus:ring-inset focus:ring-bet-green sm:text-sm sm:leading-6"
    SELECT = "block w-full rounded-md border-0 py-1.5 bg-black text-black shadow-sm ring-1 ring-inset ring-black focus:ring-2 focus:ring-inset focus:ring-bet-green sm:max-w-xs sm:text-sm sm:leading-6"
    DATE = "block px-4 w-full rounded-md border-0 py-1.5 bg-transparent text-black shadow-sm ring-1 ring-inset ring-black placeholder:text-black/10 focus:ring-2 focus:ring-inset focus:ring-bet-green sm:text-sm sm:leading-6"
    CHECKBOX = "h-4 w-4 rounded border-black text-bet-green focus:ring-bet-green"

