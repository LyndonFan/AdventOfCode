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

type InputType = [3][2]int

var buttonARegex = regexp.MustCompile(`^Button A: X\+([0-9]+), Y\+([0-9]+)$`)
var buttonBRegex = regexp.MustCompile(`^Button B: X\+([0-9]+), Y\+([0-9]+)$`)
var prizeRegex = regexp.MustCompile(`^Prize: X=([0-9]+), Y=([0-9]+)$`)

func preprocess(lines []string) ([]InputType, error) {
	res := make([]InputType, (len(lines)+1)/4)
	for i := 0; i < len(lines); i += 4 {
		var aX, aY, bX, bY, pX, pY int
		var err error
		groups := buttonARegex.FindStringSubmatch(lines[i])
		buttonAXString, buttonAYString := groups[1], groups[2]
		if aX, err = strconv.Atoi(buttonAXString); err != nil {
			return nil, err
		}
		if aY, err = strconv.Atoi(buttonAYString); err != nil {
			return nil, err
		}
		groups = buttonBRegex.FindStringSubmatch(lines[i+1])
		buttonBXString, buttonBYString := groups[1], groups[2]
		if bX, err = strconv.Atoi(buttonBXString); err != nil {
			return nil, err
		}
		if bY, err = strconv.Atoi(buttonBYString); err != nil {
			return nil, err
		}
		groups = prizeRegex.FindStringSubmatch(lines[i+2])
		prizeXString, prizeYString := groups[1], groups[2]
		if pX, err = strconv.Atoi(prizeXString); err != nil {
			return nil, err
		}
		if pY, err = strconv.Atoi(prizeYString); err != nil {
			return nil, err
		}
		res[i/4] = [3][2]int{{aX, aY}, {bX, bY}, {pX, pY}}
	}
	return res, nil
}

func solve(row InputType, costA, costB int, maxEachPresses int) int {
	// fmt.Println("solving", row, costA, costB, maxEachPresses)
	ax, ay, bx, by, tx, ty := row[0][0], row[0][1], row[1][0], row[1][1], row[2][0], row[2][1]
	if ax > tx && bx > tx {
		return 0
	}
	if ay > ty && by > ty {
		return 0
	}
	/*
		let pa, pb be no. of presses for buttons A, B.
		ax * pa + bx * pb = tx
		ay * pa + by * pb = ty
		So rewriting as matrix,
		(ax bx)(pa) = (tx)
		(ay by)(pb) = (ty)
		inverse exists iff ax*by - ay*bx != 0
		if exists,
		(pa) = ______1______ ( by -bx) (tx)
		(pb) = ax*by - ay*bx (-ay  ax) (ty)
	*/
	if det := ax*by - ay*bx; det != 0 {
		// fmt.Println("det is", det, "can solve")
		pa := (by*tx - bx*ty) / det
		pb := (-ay*tx + ax*ty) / det
		if pa < 0 || pa > maxEachPresses || pb < 0 || pb > maxEachPresses {
			return 0
		}
		if pa*ax+pb*bx != tx || pa*ay+pb*by != ty {
			return 0
		}
		return costA*pa + costB*pb
	} else {
		// fmt.Println("det is 0, can't solve yet")
		return 0
	}
}

func partA(rows []InputType) int {
	res := 0
	for _, row := range rows {
		c := solve(row, 3, 1, 100)
		// fmt.Println("cost is", c)
		res += c
	}
	return res
}

func partB(rows []InputType) int {
	res := 0
	OFFSET := 10000000000000
	for _, row := range rows {
		row[2][0] += OFFSET
		row[2][1] += OFFSET
		c := solve(row, 3, 1, OFFSET) // just need a large value since maxEachPress is no longer relevant
		// fmt.Println("cost is", c)
		res += c
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
	// fmt.Println(rows)
	partAres := partA(rows)
	fmt.Println("part A result is", partAres)
	partBres := partB(rows)
	fmt.Println("part B result is", partBres)
}

func main() {
	testFilePath := "2024/13/test.txt"
	internalMain(testFilePath)
	actualFilePath := "2024/13/input.txt"
	internalMain(actualFilePath)
}
