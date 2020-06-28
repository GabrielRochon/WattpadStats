# This file handles data slicing
def slice_reads(r):
    reads = r[:-6]                  # Removing last 6 chars (" Reads")
    return remove_commas(reads)

def slice_votes(v):
    votes = v[:-6]                  # Removing last 6 chats(" Votes")
    return remove_commas(votes)

def slice_parts(p):
    parts = p[:-11]                 # Removing last 11 chars (" Part Story")
    return remove_commas(parts)

def remove_commas(str):
    return str.replace(',', '')
