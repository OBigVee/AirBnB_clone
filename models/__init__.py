#!/usr/bin/python3
""" Creates FileStorage object for our application """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
