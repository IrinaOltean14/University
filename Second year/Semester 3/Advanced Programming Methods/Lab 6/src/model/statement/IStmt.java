package model.statement;

import model.ADT.IMyDictionary;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.type.Type;

public interface IStmt {
    PrgState execute(PrgState state) throws ADTException, ExprException, StmtException;
    IStmt deepCopy();

    IMyDictionary<String, Type> typecheck(IMyDictionary<String, Type> typeEnv) throws StmtException, ExprException, ADTException;
}
