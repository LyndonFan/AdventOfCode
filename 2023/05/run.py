# year 2023 day 5
import os
from tqdm import tqdm
import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))

class MappingLookup:
    def __init__(self, ranges: list[tuple[int, int, int]]) -> None:
        self.ranges = ranges
        self.ranges.sort(key = lambda x: x[1])
    
    def get(self, x: int) -> int:
        for destination, source, range_length in self.ranges:
            if x >= source and x < source + range_length:
                return destination + (x - source)
        return x

class FertilizerConfig:
    def __init__(
        self,
        seed_to_soil_ranges: list[tuple[int, int, int]],
        soil_to_fertilizer_ranges: list[tuple[int, int, int]],
        fertilizer_to_water_ranges: list[tuple[int, int, int]],
        water_to_light_ranges: list[tuple[int, int, int]],
        light_to_temperature_ranges: list[tuple[int, int, int]],
        temperature_to_humidity_ranges: list[tuple[int, int, int]],
        humidity_to_location_ranges: list[tuple[int, int, int]],
    ) -> None:
        self.seed_to_soil_lookup = MappingLookup(seed_to_soil_ranges)
        self.soil_to_fertilizer_lookup = MappingLookup(soil_to_fertilizer_ranges)
        self.fertilizer_to_water_lookup = MappingLookup(fertilizer_to_water_ranges)
        self.water_to_light_lookup = MappingLookup(water_to_light_ranges)
        self.light_to_temperature_lookup = MappingLookup(light_to_temperature_ranges)
        self.temperature_to_humidity_lookup = MappingLookup(temperature_to_humidity_ranges)
        self.humidity_to_location_lookup = MappingLookup(humidity_to_location_ranges)
    
    def seed_to_location(self, seed: int) -> int:
        soil = self.seed_to_soil_lookup.get(seed)
        fertilizer = self.soil_to_fertilizer_lookup.get(soil)
        water = self.fertilizer_to_water_lookup.get(fertilizer)
        light = self.water_to_light_lookup.get(water)
        temperature = self.light_to_temperature_lookup.get(light)
        humidity = self.temperature_to_humidity_lookup.get(temperature)
        location = self.humidity_to_location_lookup.get(humidity)
        return location

def parse(inp):
    data = inp.split("\n")
    seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]
    idx = 2
    ranges = {}
    while idx < len(data):
        range_name = data[idx].replace("-","_").replace(" map:","_ranges")
        idx += 1
        values = []
        while idx < len(data) and data[idx] != "":
            values.append([int(x) for x in data[idx].split(" ")])
            idx += 1
        ranges[range_name] = values
        idx += 1
    config = FertilizerConfig(**ranges)
    return seeds, config


def part_a(inp):
    seeds, config = parse(inp)
    locations = [config.seed_to_location(s) for s in seeds]
    return min(locations)


def part_b(inp):
    seeds, config = parse(inp)
    locations = []
    return min(locations)


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 35)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 46)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
