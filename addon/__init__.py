from . import config
from . import event
from .compat import compat

# Without firstrun, we no longer track the previous version.
# For compatibility with existing code, we call compat with a default.
compat("-1.-1")
