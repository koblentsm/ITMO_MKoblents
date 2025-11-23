package attacks;
import programm.Programm;
import ru.ifmo.se.pokemon.*;

import java.util.Arrays;

public final class PoisonJab extends PhysicalMove{
    public PoisonJab(){
        super(Type.POISON,80.0,100.0);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon){
        super.applyOppEffects(pokemon);
        Effect eff = new Effect();
        eff.chance(0.3).poison(pokemon);


    }

    @Override
    protected String describe(){
        return "does Poison Jab";
    }
}