import os

import psutil
import uvicorn

# Configuration Defaults
os.environ.setdefault('WEB_HOST', '0.0.0.0')
os.environ.setdefault('WEB_PORT', os.getenv('PORT', '8080'))

# Detect max web-concurrency from OS information
if 'WEB_CONCURRENCY' not in os.environ:
    os.environ['WEB_CONCURRENCY'] = str(psutil.cpu_count(logical=False) * 2 + 1)


def serve_uvicorn(app: str):
    config = uvicorn.Config(
        app=app,
        host=os.getenv('WEB_HOST'),
        port=int(os.getenv('WEB_PORT')),

        # TODO: Uvicorn has a bug with multiple workers
        # workers=int(os.getenv('WEB_CONCURRENCY')),
        workers=1,
        log_level='info',
    )

    server = uvicorn.Server(config)

    # Start Uvicorn Server
    server.run()


def serve_gunicorn(app: str):
    # This import may fail in case of non-unix based OS
    import gunicorn.app.base

    class GunicornServer(gunicorn.app.base.BaseApplication):
        def init(self, parser, opts, args) -> None:  # no-op
            pass

        def load_config(self) -> None:
            options = {
                'bind': os.getenv('WEB_HOST') + ':' + os.getenv('WEB_PORT'),
                'workers': os.getenv('WEB_CONCURRENCY'),
                'worker_class': 'uvicorn.workers.UvicornWorker',
                'preload_app': True,
                'accesslog': '-',
            }

            # Update Configuration
            for key, value in options.items():
                self.cfg.set(key, value)

        def load(self) -> str:
            return app

    # Start Gunicorn Server
    GunicornServer().run()


def serve(app: str):
    try:
        serve_gunicorn(app)
    except ImportError:
        serve_uvicorn(app)
