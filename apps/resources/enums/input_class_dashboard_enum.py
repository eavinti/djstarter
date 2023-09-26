from enum import Enum


class Input(Enum):
    TEXT = "block pl-4 w-full rounded-md border-0 py-1.5 bg-transparent text-slate-200 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-bet-green sm:text-sm sm:leading-6"
    TEXT_LEFT = "block w-full rounded-md border-0 py-1.5 pl-10 bg-transparent text-slate-200 ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-bet-green sm:text-sm sm:leading-6"
    SELECT = "block w-full rounded-md border-0 py-1.5 bg-black text-slate-200 shadow-sm ring-1 ring-inset ring-slate-300 focus:ring-2 focus:ring-inset focus:ring-bet-green sm:max-w-xs sm:text-sm sm:leading-6"
    DATE = "block pl-4 w-full rounded-md border-0 py-1.5 bg-transparent text-slate-200 shadow-sm ring-1 ring-inset ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-inset focus:ring-bet-green sm:text-sm sm:leading-6"
    CHECKBOX = "h-4 w-4 rounded border-slate-300 text-bet-green focus:ring-bet-green"

