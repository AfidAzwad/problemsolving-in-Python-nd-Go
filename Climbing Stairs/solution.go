package main

import "fmt"

func getTotalSteps(n int) int {
	one := 1
	two := 1

	for i := 1; i < n; i++ {
		temp := one
		one = one + two
		two = temp
	}

	return one
}

func main() {
	n := 5
	fmt.Println(getTotalSteps(n))
}
