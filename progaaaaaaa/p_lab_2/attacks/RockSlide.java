    package attacks;
import ru.ifmo.se.pokemon.*;
import programm.Programm;

public final class RockSlide extends PhysicalMove{
    public RockSlide(){
        super(Type.ROCK, 75.0, 90.0);
    }

    protected void applyOppEffects(Pokemon pokemon){
        super.applyOppEffects(pokemon);
        Effect eff = new Effect();
        eff.chance(0.3).flinch(pokemon);

    }
    @Override
    protected String describe(){
        return "does Rock Slide";
    }
}