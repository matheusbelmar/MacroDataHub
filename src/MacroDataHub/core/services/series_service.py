# Conteúdo de core/services/series_service.py
from core.ports.storage_port import StoragePort
from core.ports.format_port import FormatPort
from core.models.series import Series


class SeriesService:
    def __init__(self, storage_backends: list[StoragePort], format_writer: FormatPort):
        self.storage_backends = storage_backends
        self.format_writer = format_writer

    def handle_series(self, series: Series, actions: dict):
        if actions.get("return_only"):
            return series

        formatted = self.format_writer.format(series)

        if actions.get("save_local") or actions.get("save_minio"):
            for backend in self.storage_backends:
                backend.save(formatted, dest=series.path)
        return series