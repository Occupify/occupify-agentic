"""Apply limits in a fresh child, avoiding unsafe preexec_fn in the threaded app."""

import os
import resource
import sys


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (30, 32))
    resource.setrlimit(resource.RLIMIT_FSIZE, (8 * 1024 * 1024, 8 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_AS, (1024 * 1024 * 1024, 1024 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_NOFILE, (128, 128))
    os.execv(sys.argv[1], sys.argv[1:])


if __name__ == "__main__":
    main()
