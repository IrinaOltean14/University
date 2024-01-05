package model.statement;

import model.ADT.IMyDictionary;
import model.ADT.IMyStack;
import model.PrgState;
import model.exception.ADTException;
import model.exception.StmtException;
import model.type.Type;
import model.value.Value;

public class VarDeclStmt implements IStmt{
    String name;
    Type typ;

    public VarDeclStmt(String name, Type typ){
        this.name = name;
        this.typ = typ;
    }
    @Override
    public PrgState execute(PrgState state) throws ADTException,StmtException {
        IMyStack<IStmt> stack = state.getStack();
        IMyDictionary<String, Value> table = state.getDictionary();
        if (table.isDefined(name))
            throw new StmtException("The variable " + name + " is already defined");
        else{
            table.add(name, typ.defaultValue());
        }
        state.setExecutionStack(stack);
       state.setSymTable(table);
       return state;
    }

    @Override
    public IStmt deepCopy() {
        return new VarDeclStmt(new String(name), typ.deepCopy());
    }


    @Override
    public String toString(){
        return typ + " " + name;
    }
}
