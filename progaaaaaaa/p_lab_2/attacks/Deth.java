package attacks;
import ru.ifmo.se.pokemon.*;

import java.util.Arrays;

public final class Deth extends StatusMove{
    

    @Override
    protected void applySelfEffects(Pokemon pokemon) {
        pokemon.setMod(Stat.HP, (int) pokemon.getHP()+1);
        super.applySelfEffects(pokemon);
        // System.out.println(pokemon.getHP());

        //pokemon.setStats(0,0,0,0,0,0);
        //Effect eff = new Effect().stat(Stat.HP, 0);
        // //pokemon.addEffect(eff);
        // System.out.println("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr");
        // System.out.println(pokemon.getHP());
    }

    @Override
    protected String describe() {
        return "deth";
    }
}


