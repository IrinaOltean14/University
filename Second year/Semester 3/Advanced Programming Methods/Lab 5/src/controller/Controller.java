package controller;

import model.ADT.*;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.MyException;
import model.exception.StmtException;
import model.statement.*;
import model.value.RefValue;
import model.value.Value;
import repository.IRepository;
import java.util.*;
import java.io.IOException;
import java.util.stream.Collectors;

public class Controller {
    IRepository repository;

    public Controller(IRepository repository){
        this.repository = repository;
    }

    public PrgState oneStep(PrgState state) throws MyException, StmtException, ADTException, ExprException {
        IMyStack<IStmt> stack = state.getStack();
        if (stack.isEmpty())
            throw new MyException("prgstate stack is empty");
        IStmt crtStmt = stack.pop();
        return crtStmt.execute(state);
    }

    public void allStep() throws MyException, IOException {
        PrgState prg = repository.getCrtPrg();
        repository.logPrgStateExec(prg);
        while (!prg.getStack().isEmpty()){
            try{
                oneStep(prg);
                //System.out.println("Current state for the step is: ");
                //System.out.println("Execution Stack: " + prg.getStack().toString());
                //System.out.println("Symbol table: " + prg.getDictionary().toString());
                //System.out.println("Output: "+ prg.getList().toString()+ "\n");
                //repository.logPrgStateExec(prg);
                prg.getHeap().setContent((HashMap<Integer, Value>) unsafeGarbageCollector(
                        getAddrFromSymTable(prg.getDictionary().getContent().values()),
                        prg.getHeap().getContent()));
                repository.logPrgStateExec(prg);
            }
            catch (MyException | ADTException | StmtException | ExprException e){
                throw new MyException(e.getMessage());
            }
        }
    }

    public void example(IStmt example_st) throws ExprException, MyException, StmtException, ADTException, IOException {

        IMyStack<IStmt> stack = new MyStack<>();
        stack.push(example_st);
        PrgState state = new PrgState(stack, new MyDictionary<String, Value>(), new MyList<Value>(), new MyHeap());
        repository.addState(state);
        this.allStep();
    }

    Map<Integer, Value> unsafeGarbageCollector(List<Integer> symTableAddr, Map<Integer,Value> heap){
        return heap.entrySet().stream().
                filter(e -> symTableAddr.contains(e.getKey()) )
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    List<Integer> getAddrFromSymTable(Collection<Value> symTableValues){
        return symTableValues.stream()
                .filter(v-> v instanceof RefValue)
                .map(v-> {RefValue v1 = (RefValue)v; return v1.getAddr();})
                .collect(Collectors.toList());
    }
}
