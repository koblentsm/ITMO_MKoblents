package attacks;
import programm.Programm;
import ru.ifmo.se.pokemon.*;

public final class GrassWhistle extends StatusMove{
    public GrassWhistle(){
        super(Type.GRASS,0,55.0);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        super.applyOppEffects(pokemon);
        Integer randomTurns = Programm.randomInt(3);
        Effect eff = new Effect();
        eff.turns(randomTurns).sleep(pokemon);
    }

    @Override
    protected String describe(){
        return "does Grass Whistle";
    }

}