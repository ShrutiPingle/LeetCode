class Solution:
    def romanToInt(self, s: str) -> int:
        rom_list={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total_value=0
        prev_val=0

        for chh in reversed(s):
            value=rom_list[chh]
            if value<prev_val:
                total_value-=value
            else:
                total_value+=value
                prev_val=value
        return total_value