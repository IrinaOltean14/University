package model.statement;

import model.ADT.*;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.type.Type;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;

public class ForkStmt implements IStmt{
    private IStmt stmt;

    public ForkStmt(IStmt s){
        stmt = s;
    }
    @Override
    public PrgState execute(PrgState state) throws ADTException, ExprException, StmtException {
        IMyStack<IStmt> newStack = new MyStack<>();
        return new PrgState(newStack, state.getDictionary().deepCopy(), state.getList(), state.getFileTable(), state.getHeap(), stmt);
    }

    @Override
    public IStmt deepCopy() {
        return new ForkStmt(stmt.deepCopy());
    }

    @Override
    public IMyDictionary<String, Type> typecheck(IMyDictionary<String, Type> typeEnv) throws StmtException, ExprException, ADTException {
        stmt.typecheck(typeEnv.deepCopy());
        return typeEnv;
    }

    @Override
    public String toString(){
        return "fork("+stmt.toString()+")";
    }
}
