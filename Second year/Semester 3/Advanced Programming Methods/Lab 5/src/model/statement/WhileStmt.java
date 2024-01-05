package model.statement;

import model.ADT.IMyDictionary;
import model.ADT.IMyHeap;
import model.ADT.IMyStack;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.expression.Exp;
import model.type.BoolType;
import model.value.BoolValue;
import model.value.Value;

public class WhileStmt implements IStmt{
    private IStmt stmt;
    private Exp exp;

    public WhileStmt(IStmt s, Exp e){
        stmt = s;
        exp = e;
    }

    @Override
    public PrgState execute(PrgState state) throws ADTException, ExprException, StmtException {
        IMyHeap heap = state.getHeap();
        IMyStack<IStmt> stack = state.getStack();
        IMyDictionary<String, Value> symTable = state.getDictionary();

        Value expValue = exp.eval(symTable, heap);
        if (!((expValue.getType()) instanceof BoolType)){
            throw new StmtException("Expression does not evaluate to bool");
        }
        BoolValue boolValue = (BoolValue) expValue;
        if (boolValue.getVal()){
            stack.push(this);
            stack.push(stmt);
        }
        return state;
    }

    @Override
    public IStmt deepCopy() {
        return new WhileStmt(stmt.deepCopy(), exp.deepCopy());
    }

    @Override
    public String toString(){
        return "while("+exp.toString()+")"+stmt.toString();
    }
}
