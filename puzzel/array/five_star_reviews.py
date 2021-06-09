from typing import List


class AmazonFiveStarSeller:
    def get_required_five_stars(self, data: List[List[int]], threshold: int):
        result = 0
        total_products = len(data)
        target_sum = threshold * total_products * 1.0 / 100

        curr_sum = 0
        while curr_sum < target_sum:
            curr_sum = 0
            max_contribution = 0
            product_item = -1
            for i in range(0, len(data)):
                contribution = (data[i][0] + 1) * 1.0 / (data[i][1] + 1) - data[i][0] * 1.0 / data[i][1]
                if max_contribution < contribution:
                    max_contribution = contribution
                    product_item = i
                curr_sum += data[i][0] * 1.0 / data[i][1]
            curr_sum = curr_sum - data[product_item][0] * 1.0 / data[product_item][1]
            data[product_item][0] = data[product_item][0] + 1
            data[product_item][1] = data[product_item][1] + 1
            curr_sum = curr_sum + data[product_item][0] * 1.0 / data[product_item][1]
            result += 1
        return result


soln = AmazonFiveStarSeller()
print(soln.get_required_five_stars([[4, 4], [1, 2], [3, 6]], 77))
