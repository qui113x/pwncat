# Minimal shim so "import distutils.util" works on Python 3.12+/3.13
# Only implements the small pieces commonly used (e.g., get_platform).
import sys
import types

try:
    import distutils.util  # if stdlib distutils exists, do nothing
except Exception:
    import sysconfig
    shim = types.ModuleType("distutils")
    util_mod = types.ModuleType("distutils.util")

    def get_platform():
        # sysconfig.get_platform returns something like "linux-x86_64"
        return sysconfig.get_platform()

    util_mod.get_platform = get_platform

    # Put into sys.modules so "import distutils.util" works
    sys.modules["distutils"] = shim
    sys.modules["distutils.util"] = util_mod
