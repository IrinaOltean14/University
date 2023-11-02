package repository;

import model.PrgState;
import java.util.*;
public class Repository implements IRepository{
    List<PrgState> states;

    public Repository() {
        states = new ArrayList<>();
    }

    public Repository(PrgState state){
        states = new ArrayList<>();
        states.add(state);
    }

    @Override
    public PrgState getCrtPrg() {
        PrgState state = states.get(0);
        states.remove(0);
        return state;
    }

    @Override
    public List<PrgState> getPrgStates() {
        return states;
    }

    @Override
    public void addState(PrgState state) {
        states.add(state);
    }
}
