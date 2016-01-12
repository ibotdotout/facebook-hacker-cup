#!/usr/bin/env python

import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def when_file_changed(filename):
    cls()
    filename = os.path.abspath(filename)
    print(filename)
    package = ""
    if not filename.endswith("_test.py"):
        basename = os.path.basename(filename).replace(".py", "")
        package = basename
        filename = filename.replace(basename, "tests/" + basename + "_test")
    else:
        package = os.path.basename(filename).replace("_test.py", "")
    cmd = "nosetests --with-coverage --cover-erase " \
          "--cover-package={package} -v {filename}".format(**locals())
    os.system(cmd)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class ModifiedHandler(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def on_created(self, event):
        when_file_changed(event.src_path)

    def on_any_event(self, event):
        pass

    def on_modified(self, event):
        pass

if __name__ == '__main__':
    args = sys.argv[1:]
    event_handler = ModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler,
                      path=args[1] if args else '.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
