# class Solution:
#     def is_same_sequence(self, lista: list[str], listb: [list[str]]) -> bool:
#         i = j = 0
#         sa = sb = -1
#         while i < len(lista):
#             if j < len(listb):
#                 if listb[j] == "Anything" or listb[j] == lista[i]:
#                     i += 1
#                     j += 1
#                 elif listb[j] == "*":
#                     sa = j
#                     j += 1
#                     sb = i
#             if sb != -1:
#                 j = sb + 1
#                 i = ++sa
#             else:
#                 return False
#
#         while j < len(listb):
#             if not listb[j] == "*":
#                 j += 1
#                 return False
#
#         return True

# 1st loop until both index reach their size
# https://leetcode.com/discuss/interview-question/1002811/Amazon-or-OA-20201-or-Fresh-Promotion
class Solution():
    def is_same_sequence(self, orders, promotions):
        o_idx = p_idx = 0
        while p_idx < len(promotions) and o_idx < len(orders):
            # put the each promotion combination into a list
            promo_combination = promotions[p_idx]
            # initialize the above combination index
            promo_idx = 0
            # loop through the promo_combination and orders to see if
            # it satisfies
            while promo_idx < len(promo_combination) and o_idx < len(orders):
                # now compare each combination with the order and also wild card anything
                if promo_combination[promo_idx] == orders[o_idx] or promo_combination[promo_idx] == "anything":
                    # increment the promo_idx
                    promo_idx += 1
                else:
                    # if not start the comparision from beginning
                    promo_idx = 0
                # move to next order
                o_idx += 1
            if promo_idx != len(promo_combination):
                return False
            # move to next promotion combinations
            p_idx += 1
        # if the promotion index is less than total promotions
        # return False
        if p_idx < len(promotions):
            return False
        return True

    def execute(self, cart, list):
        def check(l, i):
            for k in l:
                if (k != "*" and k == cart[i]) or (k == "*"):
                    print(k, cart[i])
                    i += 1
                else:
                    return False
            return True

        vec = [False for i in range(len(list))]
        l = 0
        i = 0
        while i < len(cart) and l < len(list):
            if list[l][0] == cart[i]:
                if check(list[l], i):
                    vec[l] = True
                    i += len(list[l]) - 1
                    l += 1
            i += 1
        for i in vec:
            if not i: return i
        return True


soln = Solution()
temp = soln.is_same_sequence(["Apple", "Mango"],
                             ["Apple", "Mango"])
print(temp)
# , "*", "Banana", "Anything", "Grapes"
