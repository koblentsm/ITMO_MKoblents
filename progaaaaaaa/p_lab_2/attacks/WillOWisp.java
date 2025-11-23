package attacks;
import ru.ifmo.se.pokemon.*;

import java.util.Arrays;

public final class WillOWisp extends StatusMove{
    public WillOWisp(){
        super(Type.FIRE, 0, 85.0);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        super.applyOppEffects(pokemon);
        Effect.burn(pokemon);



    }
    @Override
    protected String describe() {
        return "does Will O Wisp";
    }
}
