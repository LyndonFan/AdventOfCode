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

func preprocess(lines []string) ([][]int, error) {
	res := make([][]int, len(lines))
	for i, line := range lines {
		parts := strings.Split(line, " ")
		a, err := strconv.Atoi(parts[0])
		if err != nil {
			return nil, err
		}
		b, err := strconv.Atoi(parts[len(parts)-1])
		if err != nil {
			return nil, err
		}
		res[i] = []int{a, b}
	}
	return res, nil
}

func partA(input [][]int) int {
	n := len(input)
	xs := make([]int, n)
	ys := make([]int, n)
	for i, nums := range input {
		xs[i] = nums[0]
		ys[i] = nums[1]
	}
	sort.Ints(xs)
	sort.Ints(ys)
	res := 0
	for i := 0; i < n; i++ {
		if xs[i] <= ys[i] {
			res += ys[i] - xs[i]
		} else {
			res += xs[i] - ys[i]
		}
	}
	return res
}

func partB(input [][]int) int {
	leftCounts := make(map[int]int)
	rightCounts := make(map[int]int)
	for _, nums := range input {
		leftCounts[nums[0]]++
		rightCounts[nums[1]]++
	}
	res := 0
	for k, v := range leftCounts {
		res += k * v * rightCounts[k]
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
	testFilePath := "2024/01/test.txt"
	actualFilePath := "2024/01/input.txt"
	internalMain(testFilePath)
	internalMain(actualFilePath)
}
