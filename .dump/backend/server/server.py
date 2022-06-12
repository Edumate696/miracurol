from __future__ import annotations

import psutil

from backend.commons.enums import Config
from backend.utils.config_utils import read_config


def is_unix() -> bool:
    try:
        import gunicorn.app.base
        return True
    except ImportError:
        # Can not load gunicorn
        return False


def auto_detect_worker_count() -> int:
    """Returns an optimum number of workers w.r.t., system configuration of the server."""
    if is_unix():
        return max(psutil.cpu_count(logical=False) * 2 + 1, 2)
    else:
        return 1  # Uvicorn has problem with multiple worker


def start_unix_server(router: str, host: str, port: int, worker_count: int):
    """Start Gunicorn Implementation for Unix based OS"""

    import gunicorn.app.base

    class GunicornStandaloneApplication(gunicorn.app.base.BaseApplication):
        """Gunicorn Stand-alone Application"""

        def __init__(self) -> None:
            self.application: str = router
            self.options: dict = {
                'bind': f'{host}:{port}',
                'workers': worker_count,
                'worker_class': 'uvicorn.workers.UvicornWorker',
                'preload_app': True,
                'accesslog': '-',
            }
            super().__init__()

        def init(self, parser, opts, args) -> None:
            pass

        def load_config(self) -> None:
            for key, value in self.options.items():
                if key in self.cfg.settings and value is not None:
                    self.cfg.set(key.lower(), value)

        def load(self) -> str:
            return self.application

    # Run App
    GunicornStandaloneApplication().run()


def start_non_unix_server(router: str, host: str, port: int, worker_count: int):
    """Start Uvicorn server Implementation for Non-Unix based OS"""

    import uvicorn

    uvicorn.run(
        app=router,
        host=host,
        port=port,  # Expects integer value
        workers=worker_count,
    )


def start_server() -> None:
    host: str = read_config(Config.SERVER.HOST) or '0.0.0.0'
    port: int = int(read_config(Config.SERVER.PORT) or 8080)
    router: str = read_config(Config.SERVER.ROUTER)
    worker_count: int = int(read_config(Config.SERVER.WORKER_COUNT) or auto_detect_worker_count())
    if is_unix():
        start_unix_server(router, host, port, worker_count)
    else:
        start_non_unix_server(router, host, port, worker_count)
