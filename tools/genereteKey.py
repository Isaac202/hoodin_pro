from hurry.filesize import size
import hashlib
import string
import random
import math


def random_key(size=5):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def generate_hash_key(salt, random_str_size=5):
    random_str = random_key(random_str_size)
    text = random_str + salt
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def file_to_shar256(file):
    bytes_file = file.read()
    shar256_hash = hashlib.sha256(bytes_file).hexdigest()
    return shar256_hash


def file_path_to_shar256(file_path):
    from py_essentials import hashing as hs
    shar256_hash = hs.fileChecksum(file_path, "sha256")
    return shar256_hash


def get_size_file(file):
    return size(file.size)


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

