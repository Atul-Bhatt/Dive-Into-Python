SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, kb_is_1024_bytes=True):
    '''
    Convert bytes to human readable form
    Arguments:
    size  -- size in bytes
    kb_is_1024_bytes -- if True use 1024 multiple else 1000
    
    '''
    
    if(size < 0):
        raise ValueError("Negative file size not allowed")
    
    base_unit = 1024 if kb_is_1024_bytes else 1000

    
    for suffix in SUFFIXES[base_unit]:
        size /= base_unit
        if(size < base_unit):
            return '{0:.1f} {1}'.format(size, suffix)
    

    raise ValueError("Number too large")




if __name__ == "__main__":
    print(approximate_size(size = 10000000, kb_is_1024_bytes=True))
    print(approximate_size(100000000, kb_is_1024_bytes=False))
    print(approximate_size(100))
    print(approximate_size(-100))