from typing import Any

class Percentile:
    def __init__(self, metric_name: Any, percentile: Any) -> None: ...
    @property
    def name(self): ...
    @property
    def percentile(self): ...