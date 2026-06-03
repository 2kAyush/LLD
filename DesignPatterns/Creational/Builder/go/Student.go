package main

import "fmt"

type Student struct {
	name   string
	age    int
	height float64
	weight float64
}

type StudentBuilder interface {
	SetName(string) StudentBuilder
	SetAge(int) StudentBuilder
	SetHeight(float64) StudentBuilder
	SetWeight(float64) StudentBuilder
	Build() *Student
}

type studentBuilder struct {
	student *Student
}

func NewStudentBuilder() StudentBuilder {
	student := Student{}
	return &studentBuilder{student: &student}
}

func (st *studentBuilder) SetName(name string) StudentBuilder {
	st.student.name = name
	return st
}
func (st *studentBuilder) SetAge(age int) StudentBuilder {
	st.student.age = age
	return st
}
func (st *studentBuilder) SetHeight(height float64) StudentBuilder {
	st.student.height = height
	return st
}
func (st *studentBuilder) SetWeight(weight float64) StudentBuilder {
	st.student.weight = weight
	return st
}

func (st *studentBuilder) Build() *Student {
	if st.student.age < 16 {
		fmt.Println("Age must be >= 16")
		return nil
	}
	return st.student
}
