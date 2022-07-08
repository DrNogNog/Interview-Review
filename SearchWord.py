# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products
#  after each character of searchWord is typed. Suggested products should 
#  have common prefix with searchWord. If there are more than three products 
#  with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

# Possible Solutions:
# Prefix Tree
# Trie
# Better Solution:
# Sort the words: Words that are sorted have common prefixes close to each other
# I will use two pointers, one located at the beginning of the array
# And a second pointer located at the end of the array.
# [mobile, money, monitor, mouse, mousepad]
# if the first and last pointer pointed to valid words for the searchword, then all words in between are thus also valid

class Solution:
    # Camel Case
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #result
        res = []
        products.sort()

        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            res.append([])
            remain = r - 1 + 1
            for j in range(min(3,remain)):
                res[-1].append(products[l + j])
        return res

#products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"

# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]





# Asymptotic - Limit (like in calculus) 
# Big Oh /Worst Case Asymptotic Upper Bound - O(1)
# Big Omega/Best Case - O(L * n * log n + m * L)   PYTHON USES TIM SORT O(N) complexity best case
# Big Theta/Best of All Worst Case - O(N^2*L)
# Space Complexity - O(n*L)