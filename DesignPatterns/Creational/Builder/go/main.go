package main

import "fmt"

func main() {
	student := NewStudentBuilder().SetName("Ayush").SetAge(15).SetHeight(178).SetWeight(70).Build()
	fmt.Println("student is: ", student)
}
