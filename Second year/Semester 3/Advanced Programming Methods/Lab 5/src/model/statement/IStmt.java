package model.statement;

import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
public interface IStmt {
    PrgState execute(PrgState state) throws ADTException, ExprException, StmtException;
    IStmt deepCopy();
}
