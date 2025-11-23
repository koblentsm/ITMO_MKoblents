package attacks;
import ru.ifmo.se.pokemon.*;

public final class FeintAttack extends PhysicalMove{
    public FeintAttack(){
        super(Type.DARK, 60.0, 100.0);
    }

    @Override
    protected String describe(){
        return "does Feint Attack";
    }
}