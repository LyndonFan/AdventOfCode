package main

import (
	"container/heap"
	"fmt"
	"os"
	"strings"
)

func parseFile(file string) ([][]int, error) {
	data, err := os.ReadFile(file)
	if err != nil {
		return nil, err
	}
	rows := strings.Split(strings.Trim(string(data), "\r\n"), "\n")
	res := make([][]int, len(rows))
	for i, row := range rows {
		res[i] = make([]int, len(row))
		for j, c := range row {
			res[i][j] = int(c - '0')
		}
	}
	return res, nil
}

type Vector [2]int

var (
	UP    Vector = [2]int{-1, 0}
	DOWN  Vector = [2]int{1, 0}
	LEFT  Vector = [2]int{0, -1}
	RIGHT Vector = [2]int{0, 1}
)
var directions = []Vector{UP, DOWN, LEFT, RIGHT}

func directionString(v Vector) string {
	if v[0] == UP[0] && v[1] == UP[1] {
		return "UP"
	} else if v[0] == DOWN[0] && v[1] == DOWN[1] {
		return "DOWN"
	} else if v[0] == LEFT[0] && v[1] == LEFT[1] {
		return "LEFT"
	} else if v[0] == RIGHT[0] && v[1] == RIGHT[1] {
		return "RIGHT"
	}
	return "UNKNOWN"
}

func (p *Vector) Add(d Vector) Vector {
	return Vector{p[0] + d[0], p[1] + d[1]}
}

type Node struct {
	Position             Vector
	Direction            Vector
	Heat                 int
	ConsecutiveStraights int8
	parent               *Node
}

func (node *Node) String() string {
	dirString := directionString(node.Direction)
	prevNode := "nil"
	if node.parent != nil {
		prevDirString := directionString(node.parent.Direction)
		prevNode = fmt.Sprintf("Node{%v, %s}", node.parent.Position, prevDirString)
	}
	return fmt.Sprintf("Node{%v, %s, %d, %d, %v}", node.Position, dirString, node.Heat, node.ConsecutiveStraights, prevNode)
}

type Heuristic func(*Node) int

func createTargetHeuristic(target Vector) Heuristic {
	return func(node *Node) int {
		return node.Heat + (target[0] - node.Position[0]) + (target[1] - node.Position[1])
	}
}

func partA(file string) (int, []*Node, error) {
	heatMap, err := parseFile(file)
	if err != nil {
		return 0, nil, err
	}
	fmt.Println("heatMap", heatMap)
	target := Vector{len(heatMap) - 1, len(heatMap[0]) - 1}
	// heuristic := func(node *Node) int { return node.Heat }
	heuristic := createTargetHeuristic(target)
	pq := make(MinHeap[*Node], 0, 4)
	rootNode := Node{
		Position:  [2]int{0, 0},
		Direction: [2]int{0, 0},
	}
	for _, d := range directions {
		node := Node{
			Position:             d,
			Direction:            d,
			ConsecutiveStraights: 1,
			parent:               &rootNode,
		}
		if node.Position[0] < 0 || node.Position[1] < 0 {
			continue
		}
		node.Heat = heatMap[node.Position[0]][node.Position[1]]
		item := &Item[*Node]{
			value:    &node,
			priority: heuristic(&node),
		}
		pq = append(pq, item)
	}
	heap.Init(&pq)
	seen := map[Vector]bool{}
	const MAX_CONSECUTIVE_STRAIGHTS = 3
	for pq.Len() > 0 {
		item := heap.Pop(&pq).(*Item[*Node])
		node := item.value
		if seen[node.Position] {
			continue
		}
		if node.ConsecutiveStraights > MAX_CONSECUTIVE_STRAIGHTS {
			continue
		}
		// fmt.Println(item.priority, node)
		seen[node.Position] = true
		if node.Position[0] == target[0] && node.Position[1] == target[1] {
			ans := node.Heat
			revPath := make([]*Node, 0, 4)
			for node.parent != nil {
				revPath = append(revPath, node)
				node = node.parent
			}
			revPath = append(revPath, node)
			path := make([]*Node, len(revPath))
			for i, nod := range revPath {
				path[len(revPath)-1-i] = nod
			}
			return ans, path, nil
		}
		for _, d := range directions {
			compareVector := node.Direction.Add(d)
			if compareVector[0] == 0 && compareVector[1] == 0 {
				continue
			}
			turned := compareVector[0] != 0 && compareVector[1] != 0
			newNode := Node{
				Position:             node.Position.Add(d),
				Direction:            d,
				Heat:                 node.Heat,
				ConsecutiveStraights: node.ConsecutiveStraights,
				parent:               node,
			}
			if newNode.Position[0] < 0 || newNode.Position[0] >= len(heatMap) {
				continue
			}
			if newNode.Position[1] < 0 || newNode.Position[1] >= len(heatMap[0]) {
				continue
			}
			newNode.Heat += heatMap[newNode.Position[0]][newNode.Position[1]]
			if turned {
				newNode.ConsecutiveStraights = 1
			} else {
				newNode.ConsecutiveStraights++
			}
			item := &Item[*Node]{
				value:    &newNode,
				priority: heuristic(&newNode),
			}
			heap.Push(&pq, item)
		}
	}
	return 0, nil, nil
}

func partB(file string) (int, error) {
	_, err := parseFile(file)
	if err != nil {
		return 0, err
	}
	return 0, nil
}

func main() {
	file := "2023/17/smolTest.txt"
	testSmol, path, err := partA(file)
	expectedSmol := 10
	if err != nil {
		fmt.Printf("Testing  (smol): Error %v\n", err)
	} else {
		fmt.Println("Path:")
		for _, p := range path {
			fmt.Println(p)
		}
		fmt.Printf("Testing  (smol): %d\n", testSmol)
		fmt.Printf("Expected (smol): %d\n", expectedSmol)
	}
	file = "2023/17/test.txt"
	testA, path, err := partA(file)
	expectedA := 102
	if err != nil {
		fmt.Printf("Testing  (a): Error %v\n", err)
	} else {
		fmt.Println("Path:")
		for _, p := range path {
			fmt.Println(p)
		}
		fmt.Printf("Testing  (a): %d\n", testA)
		fmt.Printf("Expected (a): %d\n", expectedA)
	}
	// testB, err := partB(file)
	// expectedB := -1
	// if err != nil {
	// 	fmt.Printf("Testing  (b): Error %v\n", err)
	// } else {
	// 	fmt.Printf("Testing  (b): %d\n", testB)
	// 	fmt.Printf("Expected (b): %d\n", expectedB)
	// }
	// file = "2023/17/input.txt"
	// actualA, _, err := partA(file)
	// if err != nil {
	// 	fmt.Printf("Actual   (a): Error %v\n", err)
	// } else {
	// 	fmt.Printf("Actual   (a): %d\n", actualA)
	// }
	// actualB, err := partB(file)
	// if err != nil {
	// 	fmt.Printf("Actual   (b): Error %v\n", err)
	// } else {
	// 	fmt.Printf("Actual   (b): %d\n", actualB)
	// }
}
