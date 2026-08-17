class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        store = self.hashmap[key]
        l, r = 0, len(store) - 1
        latest = ""
        #print(store)

        #print(l, r)
        while l <= r:
            mid = (l + r) // 2
            #print(store[mid])
            if store[mid][1] == timestamp:
                return store[mid][0]
            elif store[mid][1] < timestamp:
                latest = store[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return latest
