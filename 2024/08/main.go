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

func preprocess(lines []string) map[rune][][2]int {
	res := make(map[rune][][2]int)
	for i, row := range lines {
		for j, c := range row {
			if c == '.' {
				continue
			}
			if _, exists := res[c]; !exists {
				res[c] = make([][2]int, 0, 10)
			}
			res[c] = append(res[c], [2]int{i, j})
		}
	}
	return res
}

func partA(lines []string, mp map[rune][][2]int) int {
	m := len(lines)
	n := len(lines[0])
	inside := func(x, y int) bool {
		return x >= 0 && x < m && y >= 0 && y < n
	}
	res := make(map[int]bool)
	for _, poss := range mp {
		for i, s := range poss {
			for _, t := range poss[i+1:] {
				dx, dy := s[0]-t[0], s[1]-t[1]
				if inside(s[0]+dx, s[1]+dy) {
					res[n*(s[0]+dx)+s[1]+dy] = true
				}
				if inside(t[0]-dx, t[1]-dy) {
					res[n*(t[0]-dx)+t[1]-dy] = true
				}
			}
		}
	}
	return len(res)
}

func partB(lines []string, mp map[rune][][2]int) int {
	m := len(lines)
	n := len(lines[0])
	inside := func(x, y int) bool {
		return x >= 0 && x < m && y >= 0 && y < n
	}
	res := make(map[int]bool)
	for _, poss := range mp {
		for i, s := range poss {
			for _, t := range poss[i+1:] {
				res[n*s[0]+s[1]] = true
				res[n*t[0]+t[1]] = true
				dx, dy := s[0]-t[0], s[1]-t[1]
				nx, ny := s[0]+dx, s[1]+dy
				for inside(nx, ny) {
					res[n*nx+ny] = true
					nx += dx
					ny += dy
				}
				nx, ny = t[0]-dx, t[1]-dy
				for inside(nx, ny) {
					res[n*nx+ny] = true
					nx -= dx
					ny -= dy
				}
			}
		}
	}
	return len(res)
}

func internalMain(filePath string) {
	fmt.Println("running code for", filePath)
	lines, err := readLines(filePath)
	if err != nil {
		fmt.Println("failed to read", filePath, err)
		return
	}
	mp := preprocess(lines)
	partAres := partA(lines, mp)
	fmt.Println("part A result is", partAres)
	partBres := partB(lines, mp)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/08/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/08/input.txt"
	internalMain(actualFilePath)
}
