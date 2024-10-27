"""API ФНС"""

# local
from .egr import egr
from .innfl import innfl

__all__ = (
    # Данные о компании
    "egr",
    # ИНН ФЛ по ПД
    "innfl"
)

__version__ = '0.1.0'
__author__ = 'a.shilov'
