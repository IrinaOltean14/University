package repository;
import model.exception.MyException;
import model.PrgState;

import java.io.IOException;
import java.util.*;
public interface IRepository {
    PrgState getCrtPrg();
    List<PrgState> getPrgStates();

    void addState(PrgState state);

    void logPrgStateExec(PrgState state) throws MyException, IOException;
}
