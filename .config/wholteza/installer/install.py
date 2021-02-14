from src.utilities.command_line_arguments import get_distribution
from src.distribution_installer.distribution_installer_context import install


if (__name__ == "__main__"):
    install(get_distribution())
