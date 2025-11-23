package pokemons;
import attacks.Facade;
import attacks.GrassWhistle;
import attacks.PoisonJab;
import attacks.Rest;
import ru.ifmo.se.pokemon.*;

public final class Leavanny extends Swadloon{
    public Leavanny(String name, int leavl){
        super(name, leavl);
        this.setType(Type.BUG, Type.GRASS);
        this.setStats(75.0, 103.0, 80.0, 70.0, 80.0, 92.0);
        this.setMove(new Rest(), new Facade(), new GrassWhistle(), new PoisonJab());
    }
}