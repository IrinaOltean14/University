package model.statement;

import model.ADT.IMyDictionary;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.type.Type;

public class NopStmt implements IStmt{
    @Override
    public PrgState execute(PrgState state) throws StmtException {
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new NopStmt();
    }

    @Override
    public IMyDictionary<String, Type> typecheck(IMyDictionary<String, Type> typeEnv) throws StmtException, ExprException, ADTException {
        return typeEnv;
    }
}
