class Solution:
    # snake case
    #Appends all possible binary to Set then checks
    # if it is equal to 2^k num of binary
    def has_call_codes(self, s: str, k: int) -> bool:
        codeSet = set()
        for i in range(len(s) - k + 1):
            codeSet.add(s[i: i+k])
        return len(codeSet) == 2**k