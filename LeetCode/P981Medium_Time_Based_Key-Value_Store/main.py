# Problem: https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, [])
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.map.get(key, [])

        l = 0
        r = len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
