#!/usr/bin/python3
# __init__.py

import os
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
