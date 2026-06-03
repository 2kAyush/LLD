package Creational.Builder;

public class Main {
    public static void main(String[] args) {
        try {
            Student student = Student.getBuilder().set_name("Ayush").set_age(24).set_height(178).set_weight(72).build();
            System.out.println("Student: " + student);
        } catch(Exception exception) {
            System.out.println("Exception while creating object of student class");
        }
    }
}