/*
You are given an integer array nums and an integer k. You can perform the following operation any number of times:

Select an index i and replace nums[i] with nums[i] - 1.
Return the minimum number of operations required to make the sum of the array divisible by k.
*/
package main

import "fmt"

func foo(arr []int, k int) int {
	sum := 0
	for _, nums := range arr {
		sum += nums
	}
	return sum % k
}

func main() {
	arr1 := []int{1, 1, 1}
	arr2 := []int{1, 3, 6}
	fmt.Println(foo(arr1, 3))
	fmt.Println(foo(arr2, 3))
}
