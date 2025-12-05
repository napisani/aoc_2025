package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func findMaxAfter(bats []int) (int, int) {
	var max int
	var maxIndex int
	for i := 0; i < len(bats); i++ {
		if bats[i] > max {
			max = bats[i]
			maxIndex = i
		}
	}

	return max, maxIndex
}

func main() {
	fileName := "../input/day3.txt"
	file, err := os.Open(fileName)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	br := bufio.NewReader(file)

	acc := 0
	for {

		line, _, err := br.ReadLine()
		if err != nil {
			if err.Error() == "EOF" {
				break
			}
			panic(err)
		}

		cs := strings.Split(string(line), "")
		bats := make([]int, len(cs))
		for i, c := range cs {
			bats[i], err = strconv.Atoi(c)
			if err != nil {
				panic(err)
			}
		}

		numBatsToTake := 12
		highBats := []int{}
		for i := 0; i < numBatsToTake; i++ {
			fmt.Println("Iteration " + strconv.Itoa(i))
			fmt.Println("Bats: ", len(bats))
			fmt.Println("Current high bats: ", len(highBats))
			endSearchIndex := len(bats) - (numBatsToTake - len(highBats))
			fmt.Println("endSearchIndex: " + strconv.Itoa(endSearchIndex))
			searchedBats := bats[:endSearchIndex+1]
			fmt.Println("Searched bats: ", searchedBats)
			fmt.Println("all bats: ", bats)
			m, maxIndex := findMaxAfter(searchedBats)
			fmt.Println("Max bat " + strconv.Itoa(m) + " at index " + strconv.Itoa(maxIndex))
			if len(bats) > maxIndex+1 {
				bats = bats[maxIndex+1:]
			}
			highBats = append(highBats, m)
			fmt.Println("==========")
		}

		str := ""
		for _, hb := range highBats {
			str += strconv.Itoa(hb)
		}
		combinedInt, err := strconv.Atoi(str)
		if err != nil {
			panic(err)
		}
		fmt.Println("Combined: " + str)
		acc += combinedInt

		fmt.Println("High bats: ", highBats)
		fmt.Println("___________________")

		// println("Max 1: " + strM + " at index " + strconv.Itoa(mi))
		// println("Max 2: " + strM2 + " at index " + strconv.Itoa(mi2))
		// combined := strM + strM2
		// println("Combined: " + combined)
		// combinedInt, err := strconv.Atoi(combined)
		// if err != nil {
		// 	panic(err)
		// }
		// acc += combinedInt

	}
	println("Accumulator: " + strconv.Itoa(acc))
}
