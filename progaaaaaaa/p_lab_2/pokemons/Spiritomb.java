package pokemons;
import attacks.ConfuseRay;
import attacks.Facade;
import attacks.FeintAttack;
import attacks.WillOWisp;
import ru.ifmo.se.pokemon.*;

public final class Spiritomb extends Pokemon{

    public Spiritomb(String name, int leavl){
        super(name,leavl);
        this.setType(Type.GHOST, Type.DARK);
        this.setStats(50.0, 92.0, 108.0, 98.0, 108.0, 35.0);
        this.setMove(new ConfuseRay(), new FeintAttack(), new WillOWisp(), new Facade());
    }

}
