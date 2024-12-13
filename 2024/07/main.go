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

func preprocess(lines []string) ([][]int, error) {
	nums := make([][]int, len(lines))
	for i, row := range lines {
		parts := strings.Split(strings.Replace(row, ":", "", 1), " ")
		nums[i] = make([]int, len(parts))
		for j, part := range parts {
			x, err := strconv.Atoi(part)
			if err != nil {
				return nil, fmt.Errorf("error converting line %d for %s", i, part)
			}
			nums[i][j] = x
		}
	}
	return nums, nil
}

func partA(nums [][]int) int {
	res := 0
	var dfs func(int, int, int) bool
	dfs = func(row, col, curr int) bool {
		if col == 1 {
			return nums[row][1] == curr
		}
		d := nums[row][col]
		if curr < d {
			return false
		}
		if curr%d == 0 {
			if dfs(row, col-1, curr/d) {
				return true
			}
		}
		if dfs(row, col-1, curr-d) {
			return true
		}
		return false
	}
	for i := range nums {
		if dfs(i, len(nums[i])-1, nums[i][0]) {
			res += nums[i][0]
		}
	}
	return res
}

func partB(nums [][]int) int {
	res := 0
	var dfs func(int, int, int) bool
	dfs = func(row, col, curr int) bool {
		if col == 1 {
			return nums[row][1] == curr
		}
		d := nums[row][col]
		if curr < d {
			return false
		}
		if curr%d == 0 {
			if dfs(row, col-1, curr/d) {
				return true
			}
		}
		if dfs(row, col-1, curr-d) {
			return true
		}
		cString, dString := strconv.Itoa(curr), strconv.Itoa(d)
		if strings.HasSuffix(cString, dString) {
			x, _ := strconv.Atoi(cString[:len(cString)-len(dString)])
			if dfs(row, col-1, x) {
				return true
			}
		}
		return false
	}
	for i := range nums {
		if dfs(i, len(nums[i])-1, nums[i][0]) {
			res += nums[i][0]
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
	nums, err := preprocess(lines)
	if err != nil {
		fmt.Println("failed to preprocess", filePath, err)
		return
	}
	partAres := partA(nums)
	fmt.Println("part A result is", partAres)
	partBres := partB(nums)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/07/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/07/input.txt"
	internalMain(actualFilePath)
}
