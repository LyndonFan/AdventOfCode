package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readLines(filePath string) ([]string, error) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	lines := strings.Split(string(content), "\n")
	for len(lines) > 0 && lines[len(lines)-1] == "" {
		lines = lines[:len(lines)-1]
	}
	return lines, nil
}

func preprocess(lines []string) ([]int, error) {
	if len(lines) != 1 {
		return nil, fmt.Errorf("expected to have only 1 line, got %d", len(lines))
	}
	ss := strings.Split(lines[0], " ")
	res := make([]int, len(ss))
	for i, s := range ss {
		if x, err := strconv.Atoi(s); err != nil {
			return nil, fmt.Errorf("error converting for %s: %v", s, err)
		} else {
			res[i] = x
		}
	}
	return res, nil
}

func simpleBlink(stones []int, times int) []int {
	for i := 0; i < times; i++ {
		newStones := make([]int, 0, len(stones))
		for _, x := range stones {
			if x == 0 {
				newStones = append(newStones, 1)
			} else if s := strconv.Itoa(x); len(s)%2 == 0 {
				a, _ := strconv.Atoi(s[:len(s)/2])
				b, _ := strconv.Atoi(s[len(s)/2:])
				newStones = append(newStones, a)
				newStones = append(newStones, b)
			} else {
				newStones = append(newStones, x*2024)
			}
		}
		stones = newStones
	}
	return stones
}

func partA(nums []int) int {
	stones := simpleBlink(nums, 25)
	return len(stones)
}

func mapBlink(stones []int, times int) map[int]int {
	mp := make(map[int]int)
	for _, v := range stones {
		mp[v]++
	}
	for i := 0; i < times; i++ {
		newStones := make(map[int]int)
		for x, v := range mp {
			if x == 0 {
				newStones[1] += v
			} else if s := strconv.Itoa(x); len(s)%2 == 0 {
				a, _ := strconv.Atoi(s[:len(s)/2])
				b, _ := strconv.Atoi(s[len(s)/2:])
				newStones[a] += v
				newStones[b] += v
			} else {
				newStones[x*2024] += v
			}
		}
		mp = newStones
	}
	return mp
}

func partB(nums []int) int {
	stones := mapBlink(nums, 75)
	res := 0
	for _, v := range stones {
		res += v
	}
	return res
}

func internalMain(filePath string) {
	lines, err := readLines(filePath)
	if err != nil {
		return
	}
	nums, err := preprocess(lines)
	if err != nil {
		return
	}
	partAres := partA(nums)
	fmt.Println("part A result is", partAres)
	partBres := partB(nums)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/11/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/11/input.txt"
	internalMain(actualFilePath)
}
