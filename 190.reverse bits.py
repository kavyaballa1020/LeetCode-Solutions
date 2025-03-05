class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary=bin(n)[2:].zfill(32)
        reverse_str=binary[::-1]
        return int(reverse_str,2)