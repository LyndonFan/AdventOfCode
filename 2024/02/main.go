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
	res := make([][]int, len(lines))
	for i, line := range lines {
		parts := strings.Split(line, " ")
		nums := make([]int, len(parts))
		for j, p := range parts {
			a, err := strconv.Atoi(p)
			if err != nil {
				return nil, err
			}
			nums[j] = a
		}
		res[i] = nums
	}
	return res, nil
}

func isSafe(xs []int) bool {
	n := len(xs)
	switch {
	case xs[0] > xs[1]:
		for i := 0; i < n-1; i++ {
			if xs[i]-xs[i+1] <= 0 || xs[i]-xs[i+1] >= 4 {
				return false
			}
		}
		return true
	case xs[0] < xs[1]:
		for i := 0; i < n-1; i++ {
			if xs[i+1]-xs[i] <= 0 || xs[i+1]-xs[i] >= 4 {
				return false
			}
		}
		return true
	default:
		return false
	}
}

func partA(input [][]int) int {
	res := 0
	for _, xs := range input {
		if isSafe(xs) {
			res++
		}
	}
	return res
}

func partB(input [][]int) int {
	res := 0
	for _, xs := range input {
		if isSafe(xs) {
			res++
			continue
		}
		found := false
		for i := 0; !found && i < len(xs); i++ {
			ys := make([]int, len(xs)-1)
			copy(ys[:i], xs[:i])
			copy(ys[i:], xs[i+1:])
			found = isSafe(ys)
		}
		if found {
			res++
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
	inputs, err := preprocess(lines)
	if err != nil {
		fmt.Println("failed to preprocess", err)
		return
	}
	partAres := partA(inputs)
	fmt.Println("part A result is", partAres)
	partBres := partB(inputs)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/02/test.txt"
	actualFilePath := "2024/02/input.txt"
	internalMain(testFilePath)
	internalMain(actualFilePath)
}
