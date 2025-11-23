package attempt;

public class Main{
    public static void main(String args []){
        Animal a = new Animal("111111");
    }
}
class Animal{
    String name;
    Animal(String name){
        this.name = name;
        System.out.println("12");
    }
}
