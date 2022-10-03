#!/usr/bin/python3
"""adds uniq instance of FileStorage as variable storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
