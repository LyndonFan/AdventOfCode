# year 2022 day 11
import os
import re
import operator
from typing import List, Union, Tuple
from dataclasses import dataclass
from tqdm import tqdm
import logging

CWD = os.path.dirname(os.path.abspath(__file__))

monkey_pattern = r"""Monkey ([0-9]+):
  Starting items: ([0-9]+(, [0-9]+)*)
  Operation: new = old (\+|\*) (old|[0-9]+)
  Test: divisible by ([0-9]+)
    If true: throw to monkey ([0-9]+)
    If false: throw to monkey ([0-9]+)"""
monkey_pattern = re.compile(monkey_pattern)


@dataclass
class Monkey:
    id: int
    items: List[int]
    op: str
    op_arg: Union[str, int]
    div_test: int
    throw_true: int
    throw_false: int
    decrease_worry: bool = True

    def __post_init__(self) -> None:
        self.inspect_count: int = 0
        self.op = operator.add if self.op == "+" else operator.mul

    def process(self) -> Tuple[List[int], List[int]]:
        logging.debug(f"Monkey {self.id}:")
        receive_true = []
        receive_false = []
        for i in self.items:
            logging.debug(f"\tMonkey inspects an item with worry level {i}")
            if self.op_arg == "old":
                i = self.op(i, i)
                logging.debug(f"\t\tWorry level is multiplied by itself to {i}")
            else:
                i = self.op(i, self.op_arg)
                if self.op == operator.add:
                    logging.debug(
                        f"\t\tWorry level is increased by {self.op_arg} to {i}"
                    )
                else:
                    logging.debug(
                        f"\t\tWorry level is multiplied by {self.op_arg} to {i}"
                    )
            if self.decrease_worry:
                i //= 3
                logging.debug(
                    f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {i}"
                )
            if i % self.div_test == 0:
                receive_true.append(i)
                logging.debug(
                    f"\t\tCurrent worry level is divisible by {self.div_test}."
                    f"\n\t\tItem with worry level {i} is thrown to monkey {self.throw_true}."
                )
            else:
                receive_false.append(i)
                logging.debug(
                    f"\t\tCurrent worry level is not divisible by {self.div_test}."
                    f"\n\t\tItem with worry level {i} is thrown to monkey {self.throw_false}."
                )
            self.inspect_count += 1
        self.items = []
        return receive_true, receive_false


def parse(inp):
    data = inp.strip().split("\n\n")
    monkeys: List[Monkey] = []
    for m in data:
        info = monkey_pattern.search(m)
        if not info:
            print(m)
            raise ValueError(f"not found pattern:\n{m}")
        # mid, items, op, op_arg, div_test, t_true, t_false = info
        info = list(info.groups())
        info = info[:2] + info[-5:]
        # print(info)
        info[0] = int(info[0])
        info[1] = list(map(int, info[1].split(", ")))
        info[3] = "old" if info[3] == "old" else int(info[3])
        info[4] = int(info[4])
        info[5] = int(info[5])
        info[6] = int(info[6])
        monkeys.append(Monkey(*info))
    return monkeys


def part_a(inp):
    monkeys = parse(inp)
    for i in tqdm(range(20)):
        for m in monkeys:
            rtrue, rfalse = m.process()
            monkeys[m.throw_true].items += rtrue
            monkeys[m.throw_false].items += rfalse
    print([m.inspect_count for m in monkeys])
    ms = [x for x in monkeys]
    ms.sort(key=lambda m: m.inspect_count, reverse=True)
    m0, m1 = ms[:2]
    return m0.inspect_count * m1.inspect_count


def part_b(inp):
    monkeys = parse(inp)
    all_divs = 1
    for m in monkeys:
        m.decrease_worry = False
        all_divs *= m.div_test
    for i in tqdm(range(10000)):
        for m in monkeys:
            rtrue, rfalse = m.process()
            rtrue = [i % all_divs for i in rtrue]
            rfalse = [i % all_divs for i in rfalse]
            monkeys[m.throw_true].items += rtrue
            monkeys[m.throw_false].items += rfalse
    print([m.inspect_count for m in monkeys])
    ms = [x for x in monkeys]
    ms.sort(key=lambda m: m.inspect_count, reverse=True)
    m0, m1 = ms[:2]
    return m0.inspect_count * m1.inspect_count


if __name__ == "__main__":

    # logging.basicConfig(level=logging.DEBUG)

    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 10605)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 2713310158)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
