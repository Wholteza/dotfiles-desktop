import pathlib

PACKAGES_PATH_RELATIVE_TO_HOME = ".config/wholteza/installer/package-definitions"


def get_packages_definitions_directory_path():
    return pathlib.Path.home().joinpath(PACKAGES_PATH_RELATIVE_TO_HOME)
