// This example demonstrates a priority queue built using the heap interface.
package main

// borrowed from
// https://pkg.go.dev/container/heap#example-package-MinHeap
// with modifications

// An Item is something we manage in a priority queue.
type Item[T any] struct {
	value    T   // The value of the item; arbitrary.
	priority int // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A MinHeap implements heap.Interface and holds Items.
type MinHeap[T any] []*Item[T]

func (hp MinHeap[_]) Len() int { return len(hp) }

func (hp MinHeap[_]) Less(i, j int) bool {
	return hp[i].priority < hp[j].priority
}

func (hp MinHeap[_]) Swap(i, j int) {
	hp[i], hp[j] = hp[j], hp[i]
	hp[i].index = i
	hp[j].index = j
}

func (hp *MinHeap[T]) Push(x any) {
	n := len(*hp)
	item := x.(*Item[T])
	item.index = n
	*hp = append(*hp, item)
}

func (hp *MinHeap[_]) Pop() any {
	old := *hp
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*hp = old[0 : n-1]
	return item
}
