class Solution:
    def get_top_competitors(self,
                            num_competitors: int,
                            num_top_competitors: int,
                            competitors: list[str],
                            num_review: int,
                            reviews: list[str],
                            ) -> list[str]:
        freq = {}
        for competitor in competitors:
            freq[competitor] = 0

        for competitor in competitors:
            for review in reviews:
                if competitor.lower() in review.lower():
                    freq[competitor] += 1

        sorted_freq = sorted(freq, key=lambda x: [-freq[x], x])
        return sorted_freq[:num_top_competitors]


solution = Solution()
assert solution.get_top_competitors(6,
                                    2,
                                    ["newshop", "shopnow", "afashion", "fashionbeats", "mymarket", "tcellular"],
                                    6,
                                    ["newshop is providing good services in the city; everyone should use newshop",
                                     "best services by newshop",
                                     "fashionbeats has great services in the city",
                                     "I am proud to have fashionbeats",
                                     "mymarket has awesome services",
                                     "Thanks Newshop for the quick delivery"]) == ["newshop", "fashionbeats"]
