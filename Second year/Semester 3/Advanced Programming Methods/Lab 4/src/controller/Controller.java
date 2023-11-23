package controller;

import model.ADT.IMyStack;
import model.ADT.MyDictionary;
import model.ADT.MyList;
import model.ADT.MyStack;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.MyException;
import model.exception.StmtException;
import model.expression.ArithExp;
import model.expression.ValueExp;
import model.expression.VarExp;
import model.statement.*;
import model.type.BoolType;
import model.type.IntType;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.Value;
import repository.IRepository;

import java.awt.image.ImagingOpException;
import java.io.IOException;

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
        PrgState state = new PrgState(stack, new MyDictionary<String, Value>(), new MyList<Value>());
        repository.addState(state);
        this.allStep();
    }
}
