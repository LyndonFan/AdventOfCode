class RangeList:
    def __init__(self, ranges: list[tuple[int, int]]) -> None:
        self.ranges = [(s, s+l) for s,l in sorted(ranges) if l > 0]
    
    def __contains__(self, x: int) -> bool:
        return any(
            s <= x and x < e for s, e in self.ranges
        )
    
    def __len__(self) -> int:
        return sum(e-s for s,e in self.ranges)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RangeList):
            return False
        return self.ranges == other.ranges

    def __repr__(self) -> str:
        intervals_str = [f"[{s}, {e})" for s, e in self.ranges]
        return f"RangeList({', '.join(intervals_str)})"
    
    def min(self) -> int:
        if len(self) == 0:
            raise ValueError("Empty RangeList")
        for r in self.ranges:
            if r[1] > r[0]:
                return r[0]
        raise ValueError("Empty RangeList")
    
    def max(self) -> int:
        if len(self) == 0:
            raise ValueError("Empty RangeList")
        for i in range(len(self.ranges)-1, -1, -1):
            if self.ranges[i][1] > self.ranges[i][0]:
                return self.ranges[i][1] - 1
        raise ValueError("Empty RangeList")

    def copy(self) -> "RangeList":
        return RangeList([(s, e-s) for s, e in self.ranges])

    def apply_offset(self, offset: int) -> "RangeList":
        return RangeList([(s+offset, e-s) for s, e in self.ranges])

    def intersect(self, other: "RangeList") -> "RangeList":
        new_ranges = []
        self_index = 0
        other_index = 0
        while self_index < len(self.ranges) and other_index < len(other.ranges):
            self_start, self_end = self.ranges[self_index]
            other_start, other_end = other.ranges[other_index]
            if self_end <= other_start:
                self_index += 1
            elif self_start >= other_end:
                other_index += 1
            else:
                new_start = max(self_start, other_start)
                new_end = min(self_end, other_end)
                new_ranges.append((new_start, new_end - new_start))
                if self_end > other_end:
                    other_index += 1
                else:
                    self_index += 1
        return RangeList(new_ranges)
    
    def union(self, other: "RangeList") -> "RangeList":
        new_ranges = []
        self_index = 0
        other_index = 0
        while self_index < len(self.ranges) and other_index < len(other.ranges):
            self_start, self_end = self.ranges[self_index]
            other_start, other_end = other.ranges[other_index]
            if self_end < other_start:
                s, e = self.ranges[self_index]
                new_ranges.append((s, e-s))
                self_index += 1
                continue
            if self_start > other_end:
                s, e = other.ranges[other_index]
                new_ranges.append((s, e-s))
                other_index += 1
                continue
            new_start = min(self_start, other_start)
            new_end = max(self_end, other_end)
            while self_index < len(self.ranges) and other_index < len(other.ranges):
                prev_new_end = new_end
                while self_index < len(self.ranges) and self.ranges[self_index][0] <= new_end:
                    self_index += 1
                self_index -= 1
                new_end = max(self.ranges[self_index][1], new_end)
                while other_index < len(other.ranges) and other.ranges[other_index][0] <= new_end:
                    other_index += 1
                other_index -= 1
                new_end = max(other.ranges[other_index][1], new_end)
                if new_end == prev_new_end:
                    break
            new_ranges.append((new_start, new_end - new_start))
            self_index += 1
            other_index += 1
        new_ranges += [(s, e-s) for s,e in self.ranges[self_index:]]
        new_ranges += [(s, e-s) for s,e in other.ranges[other_index:]]
        return RangeList(new_ranges)

    def subtract(self, other: "RangeList") -> "RangeList":
        if not self.ranges:
            return RangeList([])
        if not other.ranges:
            return self.copy()
        if self.ranges[-1][1] <= other.ranges[0][0]:
            return self.copy()
        if other.ranges[-1][1] <= self.ranges[0][0]:
            return self.copy()
        new_ranges = []
        self_index = 0
        other_index = 0
        while self_index < len(self.ranges) and other_index < len(other.ranges):
            self_start, self_end = self.ranges[self_index]
            other_start, other_end = other.ranges[other_index]
            if self_end <= other_start:
                new_ranges.append((self_start, self_end - self_start))
                self_index += 1
                continue
            if self_start >= other_end:
                other_index += 1
                continue
            if other_start <= self_start:
                curr_start = other_end
                other_index += 1
            else:
                curr_start = self_start
            while other_index < len(other.ranges) and curr_start <= self_end:
                curr_end = other.ranges[other_index][0]
                if curr_end > curr_start:
                    new_ranges.append((curr_start, curr_end - curr_start))
                curr_start = other.ranges[other_index][1]
                other_index += 1
            if curr_start < self_end:
                new_ranges.append((curr_start, self_end - curr_start))
            self_index += 1
        new_ranges += [(s, e-s) for s,e in self.ranges[self_index:]]
        return RangeList(new_ranges)