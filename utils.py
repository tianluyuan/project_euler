"""
Useful functions
"""
def hash_answer(answer):
    """ Returns the md5 hash for checking against answers here:
    http://kmkeen.com/local-euler/project_euler.txt
    """
    import hashlib
    md5 = hashlib.md5()
    md5.update(str(answer))
    return md5.hexdigest()
