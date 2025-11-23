// class Cat {

//     public static void main (String [] args) {
    
//         System.out.println("Hello, world");
    
//     }
// }

class Main {
    public static void main(String [] args){
        // 1 способ
        Cat cat = new Cat();
        cat.saySomething();
    }

}

class Cat{
    String name = "Martin";
    int weight = 50;

    void saySomething() {
        // разобраться почему можно юзать наме
        System.out.println("My name is "+name);
    }
}