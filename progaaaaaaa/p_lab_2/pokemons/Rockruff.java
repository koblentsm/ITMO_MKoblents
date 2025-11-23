package pokemons;
import attacks.Facade;
import attacks.RockClimb;
import attacks.RockSlide;
import ru.ifmo.se.pokemon.*;
public class Rockruff extends Pokemon{
    public Rockruff(String name, int leavl){
        super(name, leavl);
        this.addType(Type.ROCK);
        this.setStats(45.0, 65.0, 40.0, 30.0, 40.0, 60.0);
        this.setMove(new Facade(), new RockClimb(), new RockSlide());
    }
}