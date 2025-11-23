package attacks;
import programm.Programm;
import ru.ifmo.se.pokemon.*;

public final class ConfuseRay extends StatusMove{
    public ConfuseRay(){
        super(Type.GHOST, 0, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon){
        Effect.confuse(pokemon);
        Effect eff2 = new Effect();
        eff2.chance(0.33).turns(Programm.randomInt(4)).stat(Stat.HP, (int)pokemon.getStat(Stat.HP)-40);
        pokemon.addEffect(eff2);
    }

    @Override
    protected String describe(){
        return "does Confuse Ray";
    }



}