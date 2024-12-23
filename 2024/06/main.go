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

func preprocess(lines []string) ([2]int, [][]bool) {
	startRow := -1
	startCol := -1
	m := len(lines[0])
	mp := make([][]bool, len(lines))
	for i, row := range lines {
		mp[i] = make([]bool, m)
		for j, c := range row {
			switch c {
			case '^':
				startRow = i
				startCol = j
			case '#':
				mp[i][j] = true
			}
		}
	}
	return [2]int{startRow, startCol}, mp
}

func partA(startPos [2]int, mp [][]bool) int {
	dr, dc := -1, 0
	n := len(mp)
	m := len(mp[0])
	row, col := startPos[0], startPos[1]
	seen := make(map[int]bool)
	for row >= 0 && row < n && col >= 0 && col < m {
		seen[m*row+col] = true
		nr, nc := row+dr, col+dc
		if !(nr >= 0 && nr < n && nc >= 0 && nc < m) {
			break
		}
		if mp[nr][nc] {
			// e.g. (dr, dc) = (-1, 0) --> (0, 1)
			// fmt.Printf("at (%d, %d): turning from (%d, %d) to (%d, %d)\n", row, col, dr, dc, -dc, dr)
			dr, dc = dc, -dr
		} else {
			row, col = nr, nc
		}
	}
	return len(seen)
}

func partB(startPos [2]int, mp [][]bool) int {
	dr, dc := -1, 0
	n := len(mp)
	m := len(mp[0])
	row, col := startPos[0], startPos[1]
	seen := make(map[int]map[int]bool)
	possible := make(map[int]bool)
	inside := func(r, c int) bool {
		return r >= 0 && r < n && c >= 0 && c < m
	}
	for inside(row, col) {
		if _, exists := seen[m*row+col]; !exists {
			seen[m*row+col] = make(map[int]bool)
		}
		seen[m*row+col][dr*3+dc] = true
		nr, nc := row+dr, col+dc
		if !inside(nr, nc) {
			break
		}
		if mp[nr][nc] {
			// e.g. (dr, dc) = (-1, 0) --> (0, 1)
			// fmt.Printf("at (%d, %d): turning from (%d, %d) to (%d, %d)\n", row, col, dr, dc, -dc, dr)
			dr, dc = dc, -dr
			continue
		}
		for i := 1; inside(row+i*dc, col-i*dr) && !mp[row+i*dc][col-i*dr]; i++ {
			if row+i*dc == startPos[0] && col-i*dr == startPos[1] {
				continue
			}
			if _, exists := seen[m*(row+i*dc)+col-i*dr][dc*3-dr]; exists {
				// fmt.Println("possible:", nr, nc, "will coinecide at", row+i*dc, col-i*dr, dc, -dr)
				possible[m*nr+nc] = true
				break
			}
		}
		row, col = nr, nc
	}
	return len(possible)
}

func internalMain(filePath string) {
	fmt.Println("running code for", filePath)
	lines, err := readLines(filePath)
	if err != nil {
		fmt.Println("failed to read", filePath, err)
		return
	}
	startPos, mp := preprocess(lines)
	fmt.Println(startPos, len(mp), len(mp[0]))
	partAres := partA(startPos, mp)
	fmt.Println("part A result is", partAres)
	partBres := partB(startPos, mp)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/06/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/06/input.txt"
	internalMain(actualFilePath)
	// for part b, 539 is too small
}
