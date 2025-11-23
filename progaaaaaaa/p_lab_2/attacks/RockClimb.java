package attacks;
import programm.Programm;
import ru.ifmo.se.pokemon.*;

public final class RockClimb extends PhysicalMove{
    public RockClimb(){
        super(Type.NORMAL, 90.0, 85.0);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon){
        super.applyOppEffects(pokemon);
        Effect eff = new Effect();
        eff.chance(0.2).confuse(pokemon);
    }

    @Override
    protected String describe(){
        return "does Rock Climb";
    }
}