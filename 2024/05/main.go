package main

import (
	"fmt"
	"os"
	"sort"
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

func preprocess(lines []string) (map[int]map[int]bool, [][]int, error) {
	numRules := 0
	for numRules < len(lines) {
		if lines[numRules] == "" {
			break
		}
		numRules++
	}
	front := make([][2]int, numRules)
	for i, row := range lines[:numRules] {
		splits := strings.Split(row, "|")
		if len(splits) != 2 {
			return nil, nil, fmt.Errorf("row %d isn't of format %%d|%%d", i)
		}
		front[i] = [2]int{0, 0}
		for j, s := range splits {
			if x, err := strconv.Atoi(s); err != nil {
				return nil, nil, fmt.Errorf("error converting row %d: %v", i, err)
			} else {
				front[i][j] = x
			}
		}
	}
	back := make([][]int, len(lines)-numRules-1)
	for i := range back {
		splits := strings.Split(lines[numRules+1+i], ",")
		back[i] = make([]int, len(splits))
		for j, s := range splits {
			if x, err := strconv.Atoi(s); err != nil {
				return nil, nil, fmt.Errorf("error converting row %d: %v", numRules+1+i, err)
			} else {
				back[i][j] = x
			}
		}
	}
	rules := getRules(front)
	return rules, back, nil
}

func getRules(front [][2]int) map[int]map[int]bool {
	// given list of a|b for a, b ints
	// returns {b: {a: true, ...}, ...}
	res := make(map[int]map[int]bool)
	for _, xs := range front {
		a := xs[0]
		b := xs[1]
		if _, exists := res[b]; !exists {
			res[b] = make(map[int]bool)
		}
		res[b][a] = true
	}
	return res
}

func orderMatchesRules(rules map[int]map[int]bool, order []int) bool {
	orderIndex := make(map[int]int)
	for i, x := range order {
		orderIndex[x] = i
	}
	for after, befores := range rules {
		idx, exists := 0, false
		if idx, exists = orderIndex[after]; !exists {
			continue
		}
		for before := range befores {
			if bidx, bexists := orderIndex[before]; bexists && bidx > idx {
				return false
			}
		}
	}
	return true
}

func partA(rules map[int]map[int]bool, orders [][]int) int {
	res := 0
	for _, order := range orders {
		if okay := orderMatchesRules(rules, order); okay {
			res += order[len(order)/2]
		}
	}
	return res
}

func fixWithRespectToRules(rules map[int]map[int]bool, order []int) []int {
	sort.Slice(order, func(i, j int) bool {
		if mp, exists := rules[order[j]]; !exists {
			return false
		} else {
			exists = mp[order[i]]
			return exists
		}
	})
	return order
}

func partB(rules map[int]map[int]bool, orders [][]int) int {
	res := 0
	for _, order := range orders {
		if okay := orderMatchesRules(rules, order); !okay {
			order = fixWithRespectToRules(rules, order)
			res += order[len(order)/2]
		}
	}
	return res
}

func internalMain(filePath string) {
	fmt.Println("running code for", filePath)
	lines, err := readLines(filePath)
	if err != nil {
		fmt.Println("failed to read", filePath, err)
		return
	}
	rules, orders, err := preprocess(lines)
	if err != nil {
		fmt.Println("failed to read", filePath, err)
		return
	}
	partAres := partA(rules, orders)
	fmt.Println("part A result is", partAres)
	partBres := partB(rules, orders)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/05/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/05/input.txt"
	internalMain(actualFilePath)
}
