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

func preprocess(lines []string) ([][]rune, error) {
	res := make([][]rune, len(lines))
	for i, row := range lines {
		res[i] = []rune(row)
	}
	return res, nil
}

func partA(rows [][]rune) int {
	regions := make(map[int][2]int) // regionID: {area, perimeter}
	m, n := len(rows), len(rows[0])
	regionIDs := make([][]int, m)
	for i := range regionIDs {
		regionIDs[i] = make([]int, n)
	}
	rid := 1
	area, perimeter := 0, 0
	var dfs func(int, int)
	directions := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	dfs = func(i, j int) {
		if regionIDs[i][j] > 0 {
			return
		}
		regionIDs[i][j] = rid
		area++
		for _, ds := range directions {
			x, y := i+ds[0], j+ds[1]
			if x < 0 || x >= m || y < 0 || y >= n || rows[x][y] != rows[i][j] {
				perimeter++
			} else {
				dfs(x, y)
			}
		}
	}
	for i, row := range rows {
		for j := range row {
			if regionIDs[i][j] > 0 {
				continue
			}
			area = 0
			perimeter = 0
			dfs(i, j)
			regions[rid] = [2]int{area, perimeter}
			rid++
		}
	}
	res := 0
	for _, vs := range regions {
		res += vs[0] * vs[1]
	}
	return res
}

func partB(rows [][]rune) int {
	m, n := len(rows), len(rows[0])
	regionIDs := make([][]int, m)
	for i := range regionIDs {
		regionIDs[i] = make([]int, n)
	}
	areas := make([]int, 0, m)
	rid := 0
	area, perimeter := 0, 0
	var dfs func(int, int)
	directions := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	dfs = func(i, j int) {
		if regionIDs[i][j] > 0 {
			return
		}
		regionIDs[i][j] = rid
		area++
		for _, ds := range directions {
			x, y := i+ds[0], j+ds[1]
			if x < 0 || x >= m || y < 0 || y >= n || rows[x][y] != rows[i][j] {
				perimeter++
			} else {
				dfs(x, y)
			}
		}
	}
	for i, row := range rows {
		for j := range row {
			if regionIDs[i][j] > 0 {
				continue
			}
			area = 0
			dfs(i, j)
			if rid >= len(areas) {
				areas = append(areas, area)
			} else {
				areas[rid] = area
			}
			rid++
		}
	}
	areas = areas[:rid]
	sides := make([]int, len(areas))
	prev := -1
	sides[regionIDs[0][n-1]]++
	for i, row := range rows {
		for _, curr := range row {
			if prev != curr {

			}
		}
		sides[regionIDs[0][0]]++

	}
	res := 0
	for _, vs := range regions {
		res += vs[0] * vs[1]
	}
	return res
}

func internalMain(filePath string) {
	lines, err := readLines(filePath)
	if err != nil {
		return
	}
	rows, err := preprocess(lines)
	if err != nil {
		return
	}
	partAres := partA(rows)
	fmt.Println("part A result is", partAres)
	// partBres := partB(rows)
	// fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/12/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/12/input.txt"
	internalMain(actualFilePath)
}
