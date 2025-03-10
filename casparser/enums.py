from enum import Enum, IntEnum, auto


class FileType(IntEnum):
    """Enum for CAS file source."""

    UNKNOWN = 0
    CAMS = 1
    KFINTECH = 2


class CASFileType(IntEnum):
    """Enum for CAS file type"""

    UNKNOWN = 0
    SUMMARY = 1
    DETAILED = 2


class TransactionType(str, Enum):
    # noinspection PyMethodParameters
    def _generate_next_value_(name, start, count, last_values) -> str:  # type: ignore
        """
        Uses the name as the automatic value, rather than an integer
        See https://docs.python.org/3/library/enum.html#using-automatic-values for reference
        """
        return name

    PURCHASE = auto()
    PURCHASE_SIP = auto()
    REDEMPTION = auto()
    DIVIDEND_PAYOUT = auto()
    DIVIDEND_REINVEST = auto()
    SWITCH_IN = auto()
    SWITCH_IN_MERGER = auto()
    SWITCH_OUT = auto()
    SWITCH_OUT_MERGER = auto()
    STT_TAX = auto()
    STAMP_DUTY_TAX = auto()
    SEGREGATION = auto()
    MISC = auto()
    UNKNOWN = auto()
    REVERSAL = auto()
