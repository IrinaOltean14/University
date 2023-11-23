package model.statement;
import model.PrgState;
import model.exception.*;
public interface IStmt {
    PrgState execute(PrgState state) throws ADTException, ExprException, StmtException;
    IStmt deepCopy();
}
