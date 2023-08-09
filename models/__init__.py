#!/usr/bin/python3
# __init__.py

import os
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()