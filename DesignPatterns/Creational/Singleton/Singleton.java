package Creational.Singleton;

class Singleton {
    public static void main(String[] args) {

    }
    String a;
    static Singleton instance = null;
    private Singleton(String a) {

    }

    public static Singleton getInstance(String a) {
        // Using Double check locking
        // but this also breaks sometimes (when serialization)
        if(instance == null) {
            // synchronized{
                if (instance == null) {
                    instance = new Singleton(a);
                }
            // }
        }
        return instance;
    }

}