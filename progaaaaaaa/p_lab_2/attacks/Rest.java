package attacks;
import ru.ifmo.se.pokemon.*;

public final class Rest extends StatusMove{
    public Rest(){
        super(Type.PSYCHIC,0,0);
    }

    @Override
    protected void applySelfEffects(Pokemon pokemon){
        Effect eff = new Effect();
        eff.turns(2).sleep(pokemon);
        pokemon.restore();

    }

    @Override
    protected String describe(){
        return "does Rest";
    }
}