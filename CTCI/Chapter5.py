"""
5.1 Insertion
"""
def insertion(N,M,i,j):
    one_mask = ~0
    left_mask = one_mask << (j+1)
    right_mask = (1 << i) - 1
    mask = left_mask | right_mask
    n_cleared = N & mask
    m_shifted = M << i
    return n_cleared | m_shifted

