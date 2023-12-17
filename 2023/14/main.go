package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type ProgressBar struct {
	current   int
	MaxVal    int
	BarLength int
}

func (p *ProgressBar) Increment() {
	p.current++
}

func (p *ProgressBar) Print() {
	toPrintString := "["
	numHashes := p.current * p.BarLength / p.MaxVal
	toPrintString += strings.Repeat("#", numHashes)
	toPrintString += strings.Repeat(" ", p.BarLength-numHashes)
	toPrintString += "]("
	maxValStringLength := len(strconv.Itoa(p.MaxVal))
	toPrintString += strings.Repeat(" ", maxValStringLength-len(strconv.Itoa(p.current)))
	toPrintString += strconv.Itoa(p.current)
	toPrintString += "/"
	toPrintString += strconv.Itoa(p.MaxVal)
	toPrintString += ")"
	fmt.Print("\r" + toPrintString)
}

func parseFile(file string) ([]string, error) {
	data, err := os.ReadFile(file)
	if err != nil {
		return nil, err
	}
	newlinePattern := regexp.MustCompile("\r?\n")
	lines := strings.Split(newlinePattern.ReplaceAllString(string(data), "\n"), "\n")
	if lines[len(lines)-1] == "" {
		lines = lines[:len(lines)-1]
	}
	return lines, nil
}

const (
	ROUND_ROCK  rune = 'O'
	CUBE_ROCK   rune = '#'
	EMPTY_SPACE rune = '.'
)

var cache map[string][]rune = make(map[string][]rune)

func rollToRight(line []rune) []rune {
	key := string(line)
	if cache[key] != nil {
		return cache[key]
	}
	res := make([]rune, len(line))
	copy(res, line)
	prevStop := -1
	numRocks := 0
	for i := 0; i < len(res); i++ {
		switch res[i] {
		case ROUND_ROCK:
			numRocks++
		case EMPTY_SPACE:
			continue
		case CUBE_ROCK:
			for d := 1; d <= numRocks; d++ {
				res[i-d] = ROUND_ROCK
			}
			for j := i - 1 - numRocks; j > prevStop; j-- {
				res[j] = EMPTY_SPACE
			}
			prevStop = i
			numRocks = 0
		}
	}
	for d := 1; d <= numRocks; d++ {
		res[len(res)-d] = ROUND_ROCK
	}
	for j := prevStop + 1; j < len(res)-numRocks; j++ {
		res[j] = EMPTY_SPACE
	}
	cache[key] = res
	return res
}

func loadOnNorthBeams(lines [][]rune) int {
	s := 0
	n := len(lines)
	for i, row := range lines {
		count := 0
		for _, c := range row {
			if c == ROUND_ROCK {
				count++
			}
		}
		s += count * (n - i)
	}
	return s
}

func partA(file string) (int, error) {
	data, err := parseFile(file)
	if err != nil {
		return 0, err
	}
	lines := make([][]rune, len(data))
	for i, row := range data {
		// fmt.Println(row)
		lines[i] = []rune(row)
	}
	n := len(lines)
	// fmt.Println(strings.Repeat("=", n))
	for i := 0; i < n; i++ {
		col := make([]rune, n)
		for j := 0; j < n; j++ {
			col[j] = lines[n-1-j][i]
		}
		col = rollToRight(col)
		for j := 0; j < n; j++ {
			lines[n-1-j][i] = col[j]
		}
	}
	// for _, row := range lines {
	// 	fmt.Println(string(row))
	// }
	// fmt.Println(strings.Repeat("=", n))
	s := loadOnNorthBeams(lines)
	return s, nil
}

func partB(file string) (int, error) {
	data, err := parseFile(file)
	if err != nil {
		return 0, err
	}
	lines := make([][]rune, len(data))
	for i, row := range data {
		lines[i] = []rune(row)
	}
	n := len(lines)
	NUM_CYCLES := 1000000000
	NUM_CYCLES /= 1000
	bar := ProgressBar{
		MaxVal:    NUM_CYCLES,
		BarLength: 60,
	}
	bar.Print()
	loadValues := make([]int, 0)
	for cycle := 0; cycle < NUM_CYCLES; cycle++ {
		startState := ""
		for _, row := range lines {
			startState += string(row)
		}
		// roll to the north
		for i := 0; i < n; i++ {
			col := make([]rune, n)
			for j := 0; j < n; j++ {
				col[j] = lines[n-1-j][i]
			}
			col = rollToRight(col)
			for j := 0; j < n; j++ {
				lines[n-1-j][i] = col[j]
			}
		}
		// roll to the west
		for i, row := range lines {
			revRow := make([]rune, len(row))
			for j := 0; j < len(row); j++ {
				revRow[j] = row[len(row)-1-j]
			}
			revRow = rollToRight(revRow)
			for j := 0; j < len(row); j++ {
				lines[i][len(row)-1-j] = revRow[j]
			}
		}
		// roll to the south
		for i := 0; i < n; i++ {
			col := make([]rune, n)
			for j := 0; j < n; j++ {
				col[j] = lines[j][i]
			}
			col = rollToRight(col)
			for j := 0; j < n; j++ {
				lines[j][i] = col[j]
			}
		}
		// roll to the east
		for i, row := range lines {
			newRow := make([]rune, len(row))
			for j := 0; j < len(row); j++ {
				newRow[j] = row[j]
			}
			newRow = rollToRight(newRow)
			for j := 0; j < len(row); j++ {
				lines[i][j] = newRow[j]
			}
		}
		bar.Increment()
		bar.Print()
		endState := ""
		for _, row := range lines {
			endState += string(row)
		}
		if startState == endState {
			break
		}
		loadValues = append(loadValues, loadOnNorthBeams(lines))
		if cycle == 0 || cycle%1000 != 0 {
			continue
		}
		NUM_CYCLES_TO_CHECK := 100
		for cycleLength := 1; cycleLength < len(loadValues)/NUM_CYCLES_TO_CHECK; cycleLength++ {
			isCycle := true
			cycleValues := loadValues[len(loadValues)-cycleLength:]
			offset := len(loadValues) - cycleLength*NUM_CYCLES_TO_CHECK
			for cycleNum := 0; cycleNum < NUM_CYCLES_TO_CHECK; cycleNum++ {
				for cIndex := 0; cIndex < cycleLength; cIndex++ {
					if loadValues[offset+cycleNum*cycleLength+cIndex] != cycleValues[cIndex] {
						isCycle = false
						break
					}
				}
				if !isCycle {
					break
				}
			}
			if isCycle {
				fmt.Println()
				fmt.Printf("Found cycle of length %d: %v\n", cycleLength, cycleValues)
				return cycleValues[(NUM_CYCLES-1-cycle)%cycleLength], nil
			}
		}
	}
	fmt.Println()
	load := loadOnNorthBeams(lines)
	return load, nil
}

func main() {
	file := "2023/14/test.txt"
	testA, err := partA(file)
	expectedA := 136
	if err != nil {
		fmt.Printf("Testing  (a): Error %v\n", err)
	} else {
		fmt.Printf("Testing  (a): %d\n", testA)
		fmt.Printf("Expected (a): %d\n", expectedA)
	}
	testB, err := partB(file)
	expectedB := 64
	if err != nil {
		fmt.Printf("Testing  (b): Error %v\n", err)
	} else {
		fmt.Printf("Testing  (b): %d\n", testB)
		fmt.Printf("Expected (b): %d\n", expectedB)
	}
	file = "2023/14/input.txt"
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
