package model;

import model.ADT.*;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.MyException;
import model.exception.StmtException;
import model.statement.IStmt;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;

public class PrgState {
    private int id;
    private static int currentId = 0;
    private IMyStack<IStmt> executionStack;
    private IMyDictionary<String, Value> symTable;
    private IMyList<Value> out;
    private IFileTable<StringValue, BufferedReader> fileTable;
    private IMyHeap heap;
    IStmt originalProgram; // optional field but good to have


    public PrgState(IMyStack<IStmt> stk, IMyDictionary<String, Value> symtbl, IMyList<Value> ot, IMyHeap heap){
        id = setId();
        executionStack = stk;
        symTable = symtbl;
        out = ot;
        this.heap = heap;
    }


    public PrgState(IMyStack<IStmt> stk, IMyDictionary<String, Value> symtbl, IMyList<Value> ot,IFileTable<StringValue, BufferedReader> fT, IMyHeap heap){
        id = setId();
        executionStack = stk;
        symTable = symtbl;
        out = ot;
        fileTable = fT;
        this.heap = heap;
        //originalProgram = prg.deepCopy();
        //stk.push(prg);
    }


    public PrgState(IMyStack<IStmt> stk, IMyDictionary<String, Value> symtbl, IMyList<Value> ot,IFileTable<StringValue, BufferedReader> fT, IMyHeap heap, IStmt stmt){
        id = setId();
        executionStack = stk;
        symTable = symtbl;
        out = ot;
        fileTable = fT;
        this.heap = heap;
        executionStack.push(stmt);
        originalProgram = stmt.deepCopy();
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


    @Override
    public String toString(){

        String representation = "";
        representation += "\n------------------\n";
        representation += "Id: " + String.valueOf(id)+"\n";
        representation += "Execution Stack: \n";
        representation += this.executionStack.toString();
        representation += "\nSymbol Table:\n";
        representation += this.symTable.toString();
        representation += "\nOutput Table:\n";
        representation += this.out.toString();
        representation += "\nFile Table:\n";
        representation += this.fileTable.toString()+ "\n";
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

    public boolean isNotCompleted(){
        return ! executionStack.isEmpty();
    }

    public PrgState oneStep() throws MyException, StmtException, ADTException, ExprException {
        if (executionStack.isEmpty())
            throw new MyException("prgstate stack is empty");
        IStmt crtStmt = executionStack.pop();
        return crtStmt.execute(this);
    }

    public synchronized int setId(){
        currentId ++;
        return currentId;
    }

}
