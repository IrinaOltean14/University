package model;

import model.ADT.IMyDictionary;
import model.ADT.IMyList;
import model.ADT.IMyStack;
import model.statement.IStmt;
import model.value.Value;

public class PrgState {
    private IMyStack<IStmt> executionStack;
    private IMyDictionary<String, Value> symTable;
    private IMyList<Value> out;
    IStmt originalProgram; // optional field but good to have
    public PrgState(IMyStack<IStmt> stk, IMyDictionary<String, Value> symtbl, IMyList<Value> ot){
        executionStack = stk;
        symTable = symtbl;
        out = ot;
    }

    public PrgState(IMyStack<IStmt> stk, IMyDictionary<String, Value> symtbl, IMyList<Value> ot, IStmt prg){
        executionStack = stk;
        symTable = symtbl;
        out = ot;
        originalProgram = prg;
        stk.push(prg);
    }

    public IMyStack<IStmt> getStack(){
        return executionStack;
    }

    public IMyDictionary<String, Value> getDictionary(){
        return symTable;
    }

    public IMyList<Value> getList(){
        return out;
    }

    public IStmt getOriginalProgram() {
        return originalProgram;
    }

    @Override
    public String toString(){
        // StringBuilder is a class in Java that provides a more efficient way to concatenate than "+"
        StringBuilder s = new StringBuilder();
        s.append("Program state\n");
        s.append("Execution stack: ").append(executionStack).append(" \n");
        s.append("Symbol Table: ").append(symTable).append("\n");
        s.append("Output: ").append(out).append("\n");
        return s.toString(); // converts the StringBuilder into a regular String
    }

    public void setExecutionStack(IMyStack<IStmt> executionStack) {
        this.executionStack = executionStack;
    }

    public void setSymTable(IMyDictionary<String, Value> symTable) {
        this.symTable = symTable;
    }

    public void setOut(IMyList<Value> out) {
        this.out = out;
    }
}
