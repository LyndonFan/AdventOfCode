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

type Draw struct {
	Red int
	Green int
	Blue int
}

type Game struct {
	ID int
	Draws []Draw
}

func gameFromLine(line string) (*Game, error) {
	parts := strings.Split(line, ": ")
	if len(parts) != 2 {
		return nil, fmt.Errorf("invalid line: %s", line)
	}
	gameID, err := strconv.Atoi(strings.Split(parts[0], " ")[1])
	if err != nil {
		return nil, err
	}
	drawStrings := strings.Split(parts[1], "; ")
	draws := make([]Draw, len(drawStrings))
	for i, drawString := range drawStrings {
		draws[i] = Draw{}
		drawParts := strings.Split(drawString, ", ")
		if len(drawParts) > 3 {
			return nil, fmt.Errorf("invalid draw: %s", drawString)
		}
		for _, drawPart := range drawParts {
			dpparts := strings.Split(drawPart, " ")
			if len(dpparts) != 2 {
				return nil, fmt.Errorf("invalid draw: %s", drawString)
			}
			num, err := strconv.Atoi(dpparts[0])
			if err != nil {
				return nil, err
			}
			switch dpparts[1] {
			case "red":
				draws[i].Red = num
			case "green":
				draws[i].Green = num
			case "blue":
				draws[i].Blue = num
			default:
				return nil, fmt.Errorf("invalid color: %s", dpparts[1])
			}
		}
	}
	return &Game{
		ID: gameID,
		Draws: draws,
	}, nil
}

const MAX_RED int = 12
const MAX_GREEN int = 13
const MAX_BLUE int = 14

func partA(file string) (int, error) {
	lines, err := parseFile(file)
	if err != nil {
		return 0, err
	}
	s := 0
	for _, line := range(lines) {
		if line == "" {
			continue
		}
		game, err := gameFromLine(line)
		if err != nil {
			return 0, err
		}
		possible := true
		for _, draw := range(game.Draws) {
			if draw.Red > MAX_RED || draw.Green > MAX_GREEN || draw.Blue > MAX_BLUE {
				possible = false
				break
			}
		}
		if possible {
			s += game.ID
		}
	}
	return s, nil
}

func partB(file string) (int, error) {
	lines, err := parseFile(file)
	if err != nil {
		return 0, err
	}
	s := 0
	for _, line := range(lines) {
		if line == "" {
			continue
		}
		game, err := gameFromLine(line)
		if err != nil {
			return 0, err
		}
		minReds := game.Draws[0].Red
		minGreens := game.Draws[0].Green
		minBlues := game.Draws[0].Blue
		for _, draw := range(game.Draws[1:]) {
			if draw.Red > minReds {
				minReds = draw.Red
			}
			if draw.Green > minGreens {
				minGreens = draw.Green
			}
			if draw.Blue > minBlues {
				minBlues = draw.Blue
			}
		}
		s += minReds * minGreens * minBlues
	}
	return s, nil
}

func main() {
	file := "2023/02/test.txt"
	testA, err := partA(file)
	expectedA := 8
	if err != nil {
		fmt.Printf("Testing  (a): Error %v\n", err)
	} else {
		fmt.Printf("Testing  (a): %d\n", testA)
		fmt.Printf("Expected (a): %d\n", expectedA)
	}
	testB, err := partB(file)
	expectedB := 2286
	if err != nil {
		fmt.Printf("Testing  (b): Error %v\n", err)
	} else {
		fmt.Printf("Testing  (b): %d\n", testB)
		fmt.Printf("Expected (b): %d\n", expectedB)
	}
	file = "2023/02/input.txt"
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
