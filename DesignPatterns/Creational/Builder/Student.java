package Creational.Builder;

import java.security.InvalidParameterException;

public class Student {
    private String name;
    private int age;
    private float height;
    private float weight;

    public String get_name(){
        return this.name;
    }

    public int get_age(){
        return this.age;
    }
    public float get_height(){
        return this.height;
    }
    public float get_weight(){
        return this.weight;
    }


    private Student() {}

    public static StudentBuilder getBuilder() {
        return new StudentBuilder();
    }

    public static class StudentBuilder {
        private String name;
        private int age;
        private float height;
        private float weight;


        public StudentBuilder set_name(String name) {
            this.name = name;
            return this;
        }
        public StudentBuilder set_age(int age) {
            this.age = age;
            return this;
        }
        public StudentBuilder set_height(float height) {
            this.height = height;
            return this;
        }
        public StudentBuilder set_weight(float weight) {
            this.weight = weight;
            return this;
        }
        public Student build() throws InvalidParameterException {
            if(this.age < 16) {
                throw new InvalidParameterException("age should be >= 16");
            }
            Student student = new Student();
            student.name = this.name;
            student.age = this.age;
            student.height = this.height;
            student.weight = this.weight;

            return student;
        }
    }

}