package repository;

import model.PrgState;
import java.util.*;
public interface IRepository {
    PrgState getCrtPrg();
    List<PrgState> getPrgStates();

    void addState(PrgState state);
}
