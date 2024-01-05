package model;

import model.ADT.*;
import model.statement.IStmt;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;

public class PrgState {
    private IMyStack<IStmt> executionStack;
    private IMyDictionary<String, Value> symTable;
    private IMyList<Value> out;
    private IFileTable<StringValue, BufferedReader> fileTable;
    private IMyHeap heap;
    IStmt originalProgram; // optional field but good to have
    public PrgState(IMyStack<IStmt> stk, IMyDictionary<String, Value> symtbl, IMyList<Value> ot, IMyHeap heap){
        executionStack = stk;
        symTable = symtbl;
        out = ot;
        this.heap = heap;
    }

    public PrgState(IMyStack<IStmt> stk, IMyDictionary<String, Value> symtbl, IMyList<Value> ot,IFileTable<StringValue, BufferedReader> fT, IMyHeap heap){
        executionStack = stk;
        symTable = symtbl;
        out = ot;
        fileTable = fT;
        this.heap = heap;
        //originalProgram = prg.deepCopy();
        //stk.push(prg);
    }

    public IMyHeap getHeap(){
        return this.heap;
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

        String representation = "";
        representation += "\n------------------\n";
        representation += "Execution Stack: \n";
        representation += this.executionStack.toString();
        representation += "\nSymbol Table:\n";
        representation += this.symTable.toString();
        representation += "\nOutput Table:\n";
        representation += this.out.toString();
        representation += "\nFile Table:\n";
        representation += this.fileTable.toString()+ "\n" ;
        representation += this.heap.toString();


        return representation;
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
    public IFileTable<StringValue, BufferedReader> getFileTable(){
        return fileTable;
    }



}
