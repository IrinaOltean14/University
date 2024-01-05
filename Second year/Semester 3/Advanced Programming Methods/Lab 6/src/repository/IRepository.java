package repository;

import model.PrgState;
import model.exception.MyException;

import java.io.IOException;
import java.util.List;
public interface IRepository {

    void addState(PrgState state);

    void logPrgStateExec(PrgState state) throws MyException, IOException;

    List<PrgState> getPrgList();

    void setPrgList(List<PrgState> l);
}
