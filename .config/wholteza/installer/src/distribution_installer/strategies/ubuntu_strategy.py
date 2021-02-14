from src.utilities.path import get_packages_definitions_directory_path
from src.package_installer.enums.package_type import PackageType
from src.package_installer.package_installer_context import ensure as ensure_packages

SNAP_PACKAGES_FILENAME = "ubuntu-snap-packages"
APT_PACKAGES_FILENAME = "ubuntu-apt-packages"

package_definitions_directory = get_packages_definitions_directory_path()


package_types = {
    PackageType.SNAP: package_definitions_directory.joinpath(SNAP_PACKAGES_FILENAME),
    PackageType.APT: package_definitions_directory.joinpath(
        APT_PACKAGES_FILENAME)
}


def install():
    """Ensures neccesary packages and configurations on ubuntu"""

    for package_type in package_types:
        ensure_packages(package_type, package_types[package_type])
    # Ensure that bashrc includes the required lines

    # Print information about what repositories to clone
