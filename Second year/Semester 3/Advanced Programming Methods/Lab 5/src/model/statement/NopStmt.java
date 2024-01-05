package model.statement;

import model.PrgState;
import model.exception.StmtException;

public class NopStmt implements IStmt{
    @Override
    public PrgState execute(PrgState state) throws StmtException {
        return state;
    }

    @Override
    public IStmt deepCopy() {
        return new NopStmt();
    }
}
