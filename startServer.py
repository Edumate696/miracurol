from backend.core.config_loader import init_configs
from backend.core.migration import run_migrations
from backend.server.server import start_server

if __name__ == '__main__':
    # Initialize all configurations
    init_configs()

    # Run Database Migration Scripts
    run_migrations()

    # Start Server
    start_server()
