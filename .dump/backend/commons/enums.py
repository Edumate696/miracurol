import enum


class Config:
    """Configurations"""

    class APP(str, enum.Enum):
        """General Application Configuration"""
        HOME = 'app.home'

    class DATABASE(str, enum.Enum):
        """Configuration for the Database"""
        URL = 'database.url'

    class SERVER(str, enum.Enum):
        """Configuration for the server environment"""
        HOST = 'server.host'
        PORT = 'server.port'
        ROUTER = 'server.router'
        WORKER_COUNT = 'server.worker.count'
