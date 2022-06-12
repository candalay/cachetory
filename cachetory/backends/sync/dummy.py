from __future__ import annotations

from datetime import datetime, timedelta
from typing import Generic, Iterable, Optional, Tuple

from cachetory.interfaces.backends.private import WireT
from cachetory.interfaces.backends.sync import SyncBackend


class DummyBackend(SyncBackend[WireT], Generic[WireT]):
    """
    Dummy backend that stores nothing.
    """

    @classmethod
    def from_url(cls, url: str) -> DummyBackend:
        return DummyBackend()

    def get(self, key: str) -> WireT:
        raise KeyError(key)

    def get_many(self, *keys: str) -> Iterable[Tuple[str, WireT]]:
        return []

    def expire_in(self, key: str, time_to_live: Optional[timedelta] = None) -> None:
        return None

    def expire_at(self, key: str, deadline: Optional[datetime]) -> None:
        return None

    def set(
        self,
        key: str,
        value: WireT,
        *,
        time_to_live: Optional[timedelta] = None,
        if_not_exists: bool = False,
    ) -> bool:
        return True

    def set_many(self, items: Iterable[Tuple[str, WireT]]) -> None:
        return None

    def delete(self, key: str) -> bool:
        return False  # has never been there

    def clear(self) -> None:
        return None  # already perfectly clean
