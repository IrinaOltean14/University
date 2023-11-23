package model.statement;

import model.ADT.IMyDictionary;
import model.ADT.IMyStack;
import model.PrgState;
import model.exception.ExprException;
import model.exception.MyException;
import model.exception.StmtException;
import model.expression.Exp;
import model.type.Type;
import model.value.*;
public class AssignStmt implements IStmt{
    String id;
    Exp exp;

    public AssignStmt(String id, Exp exp){
        this.id = id;
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) throws StmtException, ExprException {
        //IMyStack<IStmt> stack = state.getStack();
        IMyDictionary<String, Value>  table = state.getDictionary();
        if (table.isDefined(id)){
            Value val = exp.eval(table);
            Type typId = (table.lookup(id)).getType();
            if (val.getType().equals(typId)){
                table.update(id, val);
            }
            else{
                throw new StmtException("Declared type of variable " + id + " and type of the assigned expression do not match");
            }
        }
        else{
            throw new StmtException("The used variable " + id + " was not declared before");
        }
        state.setSymTable(table);
        return state;
    }

    @Override
    public IStmt deepCopy() {
        return new AssignStmt(new String(id), exp.deepCopy());
    }

    @Override
    public String toString(){
        return id + " = "+ exp.toString();
    }
}
