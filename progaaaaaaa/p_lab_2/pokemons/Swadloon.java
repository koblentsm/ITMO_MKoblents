package pokemons;
import attacks.Facade;
import attacks.GrassWhistle;
import attacks.Rest;
import attacks.Deth;
import ru.ifmo.se.pokemon.*;
public class Swadloon extends Sewaddle{
    Swadloon(String name, int leavl){
        // super(name, leavl);
        this(name, leavl, 10);
        super.setStats(55, 63.0, 90.0, 50.0, 80.0, 42.0);
        super.setMove(new Deth());
        System.out.println("1");
        // this.setStats(55, 63.0, 90.0, 50.0, 80.0, 42.0);
        // this.setMove(new Deth());

    }
    private Swadloon(String name, int leavl, int HP){
        super(name, leavl);
        System.out.println("2");
        super.setStats(HP, 63.0, 90.0, 50.0, 80.0, 42.0);
    }
}