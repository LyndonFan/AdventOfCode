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

func preprocess(lines []string) ([]int8, error) {
	if len(lines) != 1 {
		return nil, fmt.Errorf("expected to have 1 line, got %d", len(lines))
	}
	res := make([]int8, len(lines[0]))
	for i, c := range lines[0] {
		res[i] = int8(c - '0')
	}
	return res, nil
}

func checksum(xs []int16) int {
	res := 0
	for i, x := range xs {
		if x != -1 {
			res += i * int(x)
		}
	}
	return res
}

func buildInitialArray(nums []int8) []int16 {
	s := 0
	backIsBlank := true
	var backId int16 = 0
	for _, x := range nums {
		s += int(x)
		backIsBlank = !backIsBlank
		if !backIsBlank {
			backId++
		}
	}
	if backIsBlank {
		backId--
	}
	xs := make([]int16, s)
	var startId int16 = 0
	isBlank := false
	idx := 0
	for _, v := range nums {
		val := startId
		if isBlank {
			val = -1
			startId++
		}
		for i := 0; i < int(v); i++ {
			xs[idx+i] = val
		}
		idx += int(v)
		isBlank = !isBlank
	}
	if len(xs) <= 100 {
		fmt.Println(xs)
	}
	return xs
}

func partA(nums []int8) int {
	xs := buildInitialArray(nums)
	backIndex := len(xs) - 1
	idx := 0
	for idx < backIndex {
		for xs[idx] != -1 {
			idx++
		}
		for xs[backIndex] == -1 {
			backIndex--
		}
		if idx >= backIndex {
			break
		}
		for xs[idx] == -1 && xs[backIndex] != -1 {
			xs[idx], xs[backIndex] = xs[backIndex], xs[idx]
			idx++
			backIndex--
		}
	}
	if len(xs) <= 100 {
		fmt.Println(xs)
	}
	return checksum(xs)
}

func partB(nums []int8) int {
	xs := buildInitialArray(nums)
	blockStart := make([]int, (len(nums)+1)/2)
	s := 0
	isBlank := true
	for i, v := range nums {
		isBlank = !isBlank
		if !isBlank {
			blockStart[i/2] = s
		}
		s += int(v)
	}
	if len(blockStart) <= 100 {
		fmt.Println(blockStart)
	}
	for idx := len(blockStart) - 1; idx >= 0; idx-- {
		for arrIndex := 0; arrIndex < len(xs) && arrIndex+int(nums[2*idx]) < blockStart[idx]; arrIndex++ {
			for arrIndex < len(xs) && xs[arrIndex] != -1 {
				arrIndex++
			}
			if arrIndex >= blockStart[idx] {
				break
			}
			d := 1
			for xs[arrIndex+d] == -1 {
				d++
			}
			if nums[2*idx] <= int8(d) {
				for i := 0; i < int(nums[2*idx]); i++ {
					xs[arrIndex+i], xs[blockStart[idx]+i] = xs[blockStart[idx]+i], xs[arrIndex+i]
				}
				if len(xs) <= 100 {
					fmt.Println(xs)
				}
				break
			}
		}
	}
	if len(xs) <= 100 {
		fmt.Println(xs)
	}
	return checksum(xs)
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
	testFilePath := "2024/09/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/09/input.txt"
	internalMain(actualFilePath)
}
