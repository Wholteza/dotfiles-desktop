import getpass
from src.package_installer.enums.package_type import PackageType
from src.package_installer.package_installer_context import ensure as ensure_packages

username = getpass.getuser()
package_definitions_directory = "/home/% s/.config/wholteza/installers/package-definitions" % (
    username)

package_types = {
    PackageType.SNAP: package_definitions_directory + "/ubuntu-snap-packages",
    PackageType.APT: package_definitions_directory + "/ubuntu-apt-packages"
}


def install():
    """Ensures neccesary packages and configurations on ubuntu"""

    for package_type in package_types:
        ensure_packages(package_type, package_types[package_type])
    # Ensure that bashrc includes the required lines

    # Print information about what repositories to clone
