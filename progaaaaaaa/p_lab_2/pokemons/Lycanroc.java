package pokemons;
import attacks.Facade;
import attacks.RockClimb;
import attacks.RockSlide;
import attacks.SwordsDance;
import ru.ifmo.se.pokemon.*;
public final class Lycanroc extends Rockruff{
    public Lycanroc(String name, int leavl){
        super(name, leavl);
        this.addType(Type.ROCK);
        this.setStats(75.0, 115.0, 65.0, 55.0, 65.0, 112.0);
        this.setMove(new Facade(), new RockSlide(), new RockClimb(), new SwordsDance());
    }
}