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

func preprocess(lines []string) [][]byte {
	res := make([][]byte, len(lines))
	for i, s := range lines {
		res[i] = []byte(s)
	}
	return res
}

func partA(input [][]byte) int {
	target := []byte("XMAS")
	m := len(input)
	n := len(input[0])
	k := len(target)
	present := func(x, y int, ds [2]int) bool {
		if x+k*ds[0] < -1 || x+k*ds[0] > m || y+k*ds[1] < -1 || y+k*ds[1] > n {
			return false
		}
		for i, c := range target {
			if input[x+i*ds[0]][y+i*ds[1]] != c {
				return false
			}
		}
		return true
	}
	directions := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, -1}, {-1, 1}, {1, 1}, {-1, -1}}
	res := 0
	for x, row := range input {
		for y, c := range row {
			if c == target[0] {
				for _, ds := range directions {
					if present(x, y, ds) {
						res++
					}
				}
			}
		}
	}
	return res
}

func partB(input [][]byte) int {
	m := len(input)
	n := len(input[0])
	res := 0
	for x := 1; x < m-1; x++ {
		for y := 1; y < n-1; y++ {
			if input[x][y] == 'A' {
				first := input[x+1][y+1] == 'M' && input[x-1][y-1] == 'S'
				first = first || (input[x+1][y+1] == 'S' && input[x-1][y-1] == 'M')
				second := input[x-1][y+1] == 'M' && input[x+1][y-1] == 'S'
				second = second || (input[x-1][y+1] == 'S' && input[x+1][y-1] == 'M')
				if first && second {
					res++
				}
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
	input := preprocess(lines)
	partAres := partA(input)
	fmt.Println("part A result is", partAres)
	partBres := partB(input)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/04/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/04/input.txt"
	internalMain(actualFilePath)
}
