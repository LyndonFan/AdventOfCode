package main

import (
	"fmt"
	"os"
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

func preprocess(lines []string) ([][]int, error) {
	res := make([][]int, len(lines))
	for i, line := range lines {
		res[i] = make([]int, len(line))
		for j, c := range line {
			if c < '0' || c > '9' {
			}
			res[i][j] = int(c - '0')
		}
	}
	return res, nil
}

func partA(nums [][]int) int {
	m := len(nums)
	n := len(nums[0])
	canReach := make([]map[int]map[int]bool, 10)
	for i := range canReach {
		canReach[i] = make(map[int]map[int]bool)
	}
	for i, row := range nums {
		for j, x := range row {
			canReach[x][i*n+j] = make(map[int]bool)
			if x == 9 {
				canReach[x][i*n+j][i*n+j] = true
			}
		}
	}
	directions := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	inside := func(x, y int) bool {
		return x >= 0 && x < m && y >= 0 && y < n
	}
	for k := 8; k >= 0; k-- {
		for loc := range canReach[k] {
			for _, ds := range directions {
				x := loc/n + ds[0]
				y := loc%n + ds[1]
				if inside(x, y) && nums[x][y] == k+1 {
					for key := range canReach[k+1][x*n+y] {
						canReach[k][loc][key] = true
					}
				}
			}
		}
	}
	res := 0
	for _, poss := range canReach[0] {
		res += len(poss)
	}
	return res
}

func partB(nums [][]int) int {
	m := len(nums)
	n := len(nums[0])
	count := make([]map[int]int, 10)
	for i := range count {
		count[i] = make(map[int]int)
	}
	for i, row := range nums {
		for j, x := range row {
			count[x][i*n+j] = 0
			if x == 9 {
				count[x][i*n+j]++
			}
		}
	}
	directions := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	inside := func(x, y int) bool {
		return x >= 0 && x < m && y >= 0 && y < n
	}
	for k := 8; k >= 0; k-- {
		for loc := range count[k] {
			for _, ds := range directions {
				x := loc/n + ds[0]
				y := loc%n + ds[1]
				if inside(x, y) && nums[x][y] == k+1 {
					count[k][loc] += count[k+1][x*n+y]
				}
			}
		}
	}
	res := 0
	for _, val := range count[0] {
		res += val
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
	testFilePath := "2024/10/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/10/input.txt"
	internalMain(actualFilePath)
}
