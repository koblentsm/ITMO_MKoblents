package pokemons;
import attacks.Facade;
import attacks.Rest;
import ru.ifmo.se.pokemon.*;
public class Sewaddle extends Pokemon{
    public Sewaddle(String name, int leavl){
        super(name, leavl);
        this.setType(Type.BUG, Type.GRASS);
        this.setStats(45.0, 53.0, 70.0, 40.0, 60.0, 42.0);
        this.setMove(new Rest(), new Facade());
    }
}