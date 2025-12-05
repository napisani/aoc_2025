package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

type Dial struct {
	ticks        int
	timesHitZero int
}

func NewDial() Dial {
	return Dial{
		ticks: 50,
	}
}

func (d *Dial) turn(dist int) {
	for i := 0; i < Abs(dist); i++ {
		if dist < 0 {
			d.ticks--
		} else {
			d.ticks++
		}
		if d.ticks >= 100 {
			d.ticks = 0
			d.timesHitZero++
		} else if d.ticks == 0 {
			d.timesHitZero++
		} else if d.ticks < 0 {
			d.ticks = 99
		}

	}

}

func (d *Dial) TurnLeft(dist int) {
	dist = dist * -1
	d.turn(dist)
}

func (d *Dial) TurnRight(dist int) {
	d.turn(dist)
}

func (d *Dial) Count() int {
	return d.timesHitZero
}

func main() {
	ticks := 50
	fileName := "../input/day1.txt"
	file, err := os.Open(fileName)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	br := bufio.NewReader(file)
	zeros := 0
	fmt.Println(ticks)
	dial := NewDial()
	for {
		line, _, err := br.ReadLine()
		if err != nil {
			if err.Error() == "EOF" {
				break
			}
			panic(err)
		}
		dir := string(line)[0]
		dist, err := strconv.Atoi(string(line)[1:])

		fmt.Printf("Direction: %c Distance: %d\n", dir, dist)
		ticksBefore := ticks

		if err != nil {
			panic(err)
		}
		originalDist := dist
		dist = dist % 100
		if dir == 'L' {
			dist = dist * -1
			originalDist = originalDist * -1
			dial.TurnLeft(Abs(originalDist))
		} else {
			dial.TurnRight(Abs(originalDist))
		}

		if (ticks+dist) >= 100 || (ticks+dist) < 0 {
			r := Abs((ticks + dist) % 100)

			if dist < 0 {
				ticks = 100 - r

			} else {
				ticks = r
			}

		} else {
			ticks = ticks + dist
		}

		fmt.Printf("Ticks before: %d \n", ticksBefore)
		fmt.Printf("Resulting ticks: %d \n", ticks)

		// pt1
		if ticks == 0 {
			zeros++
		}

		fmt.Println("zeros so far:", dial.Count())
		println("----")
	}
	// pt2
	fmt.Printf("Total zeros: %d \n", dial.Count())
	fmt.Printf("Total zeros (old way): %d \n", zeros)

}
