package main

import (
	"fmt"
	"image"
	"image/png"
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

type InputType = []int

var lineRegex = regexp.MustCompile(`^p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)$`)

func preprocess(lines []string) ([]InputType, error) {
	res := make([]InputType, len(lines))
	for i, line := range lines {
		if !lineRegex.MatchString(line) {
			return nil, fmt.Errorf("error parsing line %d: %s: failed to match pattern", i, line)
		}
		groups := lineRegex.FindStringSubmatch(line)
		inps := make([]int, 4)
		for j, v := range groups[1:] {
			if x, err := strconv.Atoi(v); err != nil {
				return nil, fmt.Errorf("error parsing line %d: %s: failed to parse %s to int: %v", i, line, v, err)
			} else {
				inps[j] = x
			}
		}
		res[i] = inps
	}
	return res, nil
}

func genPos(rows []InputType, seconds, width, height int) [][2]int {
	poss := make([][2]int, len(rows))
	for i, row := range rows {
		x := (row[0] + row[2]*seconds) % width
		if x < 0 {
			x += width
		}
		y := (row[1] + row[3]*seconds) % height
		if y < 0 {
			y += height
		}
		poss[i] = [2]int{x, y}
	}
	return poss
}

func partA(rows []InputType) int {
	var poss [][2]int
	var width, height int
	if len(rows) <= 50 {
		width, height = 11, 7
	} else {
		width, height = 101, 103
	}
	poss = genPos(rows, 100, width, height)
	qs := make([]int, 4)
	for _, pos := range poss {
		x, y := pos[0], pos[1]
		index := 0
		if x == width/2 || y == height/2 {
			continue
		}
		if x > width/2 {
			index++
		}
		if y > height/2 {
			index += 2
		}
		qs[index]++
	}
	fmt.Println(qs)
	return qs[0] * qs[1] * qs[2] * qs[3]
}

func saveImage(poss [][2]int, width, height, i int) error {
	img := image.NewRGBA(image.Rect(0, 0, width, height))
	for _, pos := range poss {
		img.Pix[4*(pos[0]+pos[1]*width)+1] = 255
		img.Pix[4*(pos[0]+pos[1]*width)+3] = 255
	}
	file, err := os.Create(fmt.Sprintf("2024/14/%06d.png", i))
	if err != nil {
		return err
	}
	png.Encode(file, img)
	file.Close()
	return nil
}

func hasOverlaps(poss [][2]int, width int) bool {
	seen := make(map[int]bool)
	for _, pos := range poss {
		if k := pos[0] + pos[1]*width; seen[k] {
			return true
		} else {
			seen[k] = true
		}
	}
	return false
}

const MAX_STEPS int = 100000

func partB(rows []InputType) int {
	if len(rows) <= 50 {
		fmt.Println("Skipped")
		return 0
	}
	poss := make([][2]int, len(rows))
	width, height := 101, 103
	for i, row := range rows {
		poss[i] = [2]int{row[0], row[1]}
	}
	count := 0
	// had to google to know
	// check image for lack of overlaps --> xmas tree appears
	for ; count <= MAX_STEPS && hasOverlaps(poss, width); count++ {
		for i, row := range rows {
			poss[i][0] = (poss[i][0] + row[2] + width) % width
			poss[i][1] = (poss[i][1] + row[3] + height) % height
		}
	}
	saveImage(poss, width, height, count)
	return count
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
	// fmt.Println(rows)
	partAres := partA(rows)
	fmt.Println("part A result is", partAres)
	partBres := partB(rows)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/14/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/14/input.txt"
	internalMain(actualFilePath)
}
