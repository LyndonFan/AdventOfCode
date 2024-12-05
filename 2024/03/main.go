package main

import (
	"fmt"
	"os"
	"regexp"
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

var pattern = regexp.MustCompile(`mul\([0-9]{1,3},[0-9]{1,3}\)`)

func partA(lines []string) int {
	res := 0
	for _, line := range lines {
		matches := pattern.FindAll([]byte(line), -1)
		for _, matchBytes := range matches {
			match := strings.Replace(strings.Replace(string(matchBytes), "mul(", "", -1), ")", "", -1)
			numbers := strings.Split(match, ",")
			a, err := strconv.Atoi(numbers[0])
			if err != nil {
				panic(err)
			}
			b, err := strconv.Atoi(numbers[1])
			if err != nil {
				panic(err)
			}
			res += a * b
		}
	}
	return res
}

var togglePattern = regexp.MustCompile(`mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)`)

func partB(lines []string) int {
	res := 0
	line := strings.Join(lines, "\n")
	enabled := true
	matches := togglePattern.FindAll([]byte(line), -1)
	for _, matchBytes := range matches {
		switch string(matchBytes) {
		case "do()":
			enabled = true
		case "don't()":
			enabled = false
		default:
			if enabled {
				match := strings.Replace(strings.Replace(string(matchBytes), "mul(", "", -1), ")", "", -1)
				numbers := strings.Split(match, ",")
				a, err := strconv.Atoi(numbers[0])
				if err != nil {
					panic(err)
				}
				b, err := strconv.Atoi(numbers[1])
				if err != nil {
					panic(err)
				}
				res += a * b
			}
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
	if err != nil {
		fmt.Println("failed to preprocess", err)
		return
	}
	partAres := partA(lines)
	fmt.Println("part A result is", partAres)
	partBres := partB(lines)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/03/test.txt"
	actualFilePath := "2024/03/input.txt"
	internalMain(testFilePath)
	testFilePath = "2024/03/testB.txt"
	internalMain(testFilePath)
	internalMain(actualFilePath)
}
