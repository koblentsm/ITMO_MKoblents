package attacks;
import ru.ifmo.se.pokemon.*;

public final class Facade extends PhysicalMove {
    public Facade() {
        super(Type.NORMAL, 70.0, 100.0);
    }


    @Override
    protected void applySelfEffects(Pokemon pokemon){
        super.applySelfEffects(pokemon);
        if (pokemon.getCondition() == Status.BURN || pokemon.getCondition() == Status.POISON || pokemon.getCondition() == Status.PARALYZE){
            Effect eff = new Effect().turns(1).stat(Stat.ATTACK, 140);
            pokemon.addEffect(eff);
        }
    }

    @Override
    protected String describe(){
        return "does Facade";
    }

}