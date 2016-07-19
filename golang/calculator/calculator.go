package main

import (
	"./stack"
	"bufio"
	"fmt"
	"os"
)

func main() {
	//m := new(stack.Stack)
	flag := true
	var lineStr string
	for flag {
		bio := bufio.NewReader(os.Stdin)
		line, _, err := bio.ReadLine()
		lineStr = string(line)
		if err == nil && lineStr != "quit" {
			fmt.Printf("%v\n", lineStr)
		}
	}
}
