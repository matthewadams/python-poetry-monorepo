import sys
import nanoid
from datetime import datetime, timezone

def stdout(it):
    print(str(it))


def stderr(it):
    print(str(it), file=sys.stderr)


# from platform lib.core.utils.Nano
default_nanoid_alphabet = "23456789abcdefghijkmnpqrstuvwxy"
default_nanoid_length = 27


def nano_id():
    return nanoid.generate(default_nanoid_alphabet, default_nanoid_length)


def ts(dt: datetime = datetime.now(timezone.utc)):
    return dt.astimezone(timezone.utc).replace(tzinfo=None).isoformat(timespec='seconds') + 'Z'
