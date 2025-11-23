package attacks;
import ru.ifmo.se.pokemon.*;

public final class SwordsDance extends StatusMove{
    public SwordsDance(){
        super(Type.NORMAL,0,0);
    }

    @Override
    protected void applySelfEffects(Pokemon pokemon){
        super.applySelfEffects(pokemon);
        Effect eff = new Effect().stat(Stat.ATTACK, 2);
        pokemon.addEffect(eff);
    }

    @Override
    protected String describe(){
        return "does Swords Dance";
    }
}