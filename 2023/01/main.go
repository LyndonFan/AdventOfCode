package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func parseFile(file string) ([]string, error) {
	data, err := os.ReadFile(file)
	if err != nil {
		return nil, err
	}
	newlinePattern := regexp.MustCompile("\r?\n")
	lines := strings.Split(newlinePattern.ReplaceAllString(string(data), "\n"), "\n")
	return lines, nil
}

func partA(file string) (int, error) {
	lines, err := parseFile(file)
	if err != nil {
		return 0, err
	}
	twoNumberPattern := regexp.MustCompile(`^[a-z]*(\d).*(\d)[a-z]*$`)
	oneNumberPattern := regexp.MustCompile(`^[a-z]*(\d)[a-z]*$`)
	s := 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		matches := twoNumberPattern.FindStringSubmatch(line)
		if len(matches) == 3 {
			n1, _ := strconv.Atoi(matches[1])
			n2, _ := strconv.Atoi(matches[2])
			s += n1*10 + n2
		} else {
			matches = oneNumberPattern.FindStringSubmatch(line)
			if len(matches) == 2 {
				n, _ := strconv.Atoi(matches[1])
				s += n * 11
			} else {
				return 0, fmt.Errorf("invalid line: %s", line)
			}
		}
	}
	return s, nil
}

var numberStrings = [10]string{
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
}

func partB(file string) (int, error) {
	lines, err := parseFile(file)
	if err != nil {
		return 0, err
	}
	s := 0
	for _, line := range lines {
		if line == "" {
			continue
		}
		firstNum, secondNum := -1, -1
		for i := 0; i < len(line); i++ {
			if '0' <= line[i] && line[i] <= '9' {
				firstNum = int(line[i] - '0')
				break
			}
			for j := 0; j < 10; j++ {
				if i+len(numberStrings[j]) <= len(line) && line[i:i+len(numberStrings[j])] == numberStrings[j] {
					firstNum = j
					break
				}
			}
			if firstNum != -1 {
				break
			}
		}
		for i := len(line) - 1; i >= 0; i-- {
			if '0' <= line[i] && line[i] <= '9' {
				secondNum = int(line[i] - '0')
				break
			}
			for j := 0; j < 10; j++ {
				if i+len(numberStrings[j]) <= len(line) && line[i:i+len(numberStrings[j])] == numberStrings[j] {
					secondNum = j
					break
				}
			}
			if secondNum != -1 {
				break
			}
		}
		s += firstNum*10 + secondNum
	}
	return s, nil
}

func main() {
	file := "2023/01/test_a.txt"
	testA, err := partA(file)
	expectedA := 142
	if err != nil {
		fmt.Printf("Testing  (a): Error %v\n", err)
	} else {
		fmt.Printf("Testing  (a): %d\n", testA)
		fmt.Printf("Expected (a): %d\n", expectedA)
	}
	file = "2023/01/test_b.txt"
	testB, err := partB(file)
	expectedB := 281
	if err != nil {
		fmt.Printf("Testing  (b): Error %v\n", err)
	} else {
		fmt.Printf("Testing  (b): %d\n", testB)
		fmt.Printf("Expected (b): %d\n", expectedB)
	}
	file = "2023/01/input.txt"
	actualA, err := partA(file)
	if err != nil {
		fmt.Printf("Actual   (a): Error %v\n", err)
	} else {
		fmt.Printf("Actual   (a): %d\n", actualA)
	}
	actualB, err := partB(file)
	if err != nil {
		fmt.Printf("Actual   (b): Error %v\n", err)
	} else {
		fmt.Printf("Actual   (b): %d\n", actualB)
	}
}
