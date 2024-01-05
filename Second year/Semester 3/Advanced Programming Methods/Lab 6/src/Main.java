import controller.Controller;
import model.ADT.*;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.expression.*;
import model.statement.*;
import model.type.IntType;
import model.type.RefType;
import model.type.Type;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;
import repository.*;
import model.*;
import view.ExitCommand;
import view.RunExample;
import view.TextMenu;
import java.io.BufferedReader;


public class Main {
    public static void main(String[] args) throws ExprException, StmtException, ADTException {

        TextMenu menu = new TextMenu();
        IMyStack<IStmt> stack1 = new MyStack<>();

        IStmt example_1 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ValueExp(new IntValue(17))),
                        new PrintStmt(new VarExp("x"))
                )
        );
        try{
            example_1.typecheck(new MyDictionary<String, Type>());
            stack1.push(example_1);
            PrgState prg1 = new PrgState(stack1, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo1 = new Repository(prg1, "log1.txt");
            Controller ctr1 = new Controller(repo1);
            menu.addCommand(new RunExample("1", example_1.toString(), ctr1));
        } catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }

        IMyStack<IStmt> stack2 = new MyStack<>();
        IStmt example2 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ArithExp('+', new ValueExp(new IntValue(5)), new ValueExp(new IntValue(7)))),
                        new PrintStmt(new VarExp("x"))
                )
        );
        try{
            example2.typecheck(new MyDictionary<String, Type>());
            stack2.push(example2);
            PrgState prg2 = new PrgState(stack2, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo2 = new Repository(prg2, "log2.txt");
            Controller ctr2 = new Controller(repo2);
            menu.addCommand(new RunExample("2", example2.toString(), ctr2));
        } catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }


        IMyStack<IStmt> stack3 = new MyStack<>();
        IStmt example_3 = new CompStmt(
                new VarDeclStmt("a", new IntType()),
                new CompStmt(
                        new VarDeclStmt("b", new IntType()),
                        new CompStmt(
                                new AssignStmt("a", new ValueExp(new IntValue(10))),
                                new CompStmt(
                                        new AssignStmt("b", new ValueExp(new IntValue(9))),
                                        new IfStmt(new RelationalExp(1,new VarExp("a"), new VarExp("b")), new PrintStmt(new ValueExp(new StringValue("a is smaller"))), new PrintStmt(new ValueExp(new StringValue("b is smaller"))))
                                )
                        )
                )
        );
        try{
            example_3.typecheck(new MyDictionary<String, Type>());
            stack3.push(example_3);
            PrgState prg3 = new PrgState(stack3,new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo3 = new Repository(prg3, "log3.txt");
            Controller ctr3 = new Controller(repo3);
            menu.addCommand(new RunExample("3", example_3.toString(), ctr3));
        }
        catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }


        IMyStack<IStmt> stack4 = new MyStack<>();
        IStmt example_4 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ValueExp(new BoolValue(true))),
                        new PrintStmt(new VarExp("x"))
                )
        );
        try{
            example_4.typecheck(new MyDictionary<String, Type>());
            stack4.push(example_4);
            PrgState prg4 = new PrgState(stack4,new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo4 = new Repository(prg4, "log4.txt");
            Controller ctr4 = new Controller(repo4);
            menu.addCommand(new RunExample("4", example_4.toString(), ctr4));
        }
        catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }

        IMyStack<IStmt> stack5 = new MyStack<>();
        IStmt example_5 = new CompStmt(
                new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(
                        new NewStmt("v", new ValueExp(new IntValue(20))),
                        new CompStmt(
                                new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(
                                        new NewStmt("a", new VarExp("v")),
                                        new CompStmt(
                                                new PrintStmt(new VarExp("v")),
                                                new PrintStmt(new VarExp("a"))
                                        )
                                )
                        )
                )
        );
        try{
            example_5.typecheck(new MyDictionary<String, Type>());
            stack5.push(example_5);
            PrgState prg5 = new PrgState(stack5, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo5 = new Repository(prg5, "log5.txt");
            Controller ctr5 = new Controller(repo5);
            menu.addCommand(new RunExample("5", example_5.toString(), ctr5));
        }
        catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }


        IMyStack<IStmt> stack6 = new MyStack<>();
        IStmt example_6 = new CompStmt(
                new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(
                        new NewStmt("v",new ValueExp(new IntValue(20))),
                        new CompStmt(
                                new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(
                                        new NewStmt("a", new VarExp("v")),
                                        new CompStmt(
                                                new PrintStmt(new HeapReadingExp(new VarExp("v"))),
                                                new PrintStmt(new ArithExp('+', new HeapReadingExp(new HeapReadingExp(new VarExp("a"))), new ValueExp(new IntValue(5))))
                                        )
                                )
                        )
                )
        );
        try{
            example_5.typecheck(new MyDictionary<String, Type>());
            stack6.push(example_6);
            PrgState prg6 = new PrgState(stack6, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo6 = new Repository(prg6, "log6.txt");
            Controller ctr6 = new Controller(repo6);
            menu.addCommand(new RunExample("6", example_6.toString(), ctr6));
        }
        catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }


        IMyStack<IStmt> stack7 = new MyStack<>();
        IStmt example_7 = new CompStmt(
                new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(
                        new NewStmt("v", new ValueExp(new IntValue(20))),
                        new CompStmt(
                                new PrintStmt(new HeapReadingExp(new VarExp("v"))),
                                new CompStmt(
                                        new HeapWritingStmt("v", new ValueExp(new IntValue(30))),
                                        new PrintStmt(new ArithExp('+',new HeapReadingExp(new VarExp("v")), new ValueExp(new IntValue(5))))
                                )
                        )
                )
        );
        try{
            example_7.typecheck(new MyDictionary<String, Type>());
            stack7.push(example_7);
            PrgState prg7 = new PrgState(stack7, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo7 = new Repository(prg7, "log7.txt");
            Controller ctr7 = new Controller(repo7);
            menu.addCommand(new RunExample("7", example_7.toString(), ctr7));
        }
        catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }

        IMyStack<IStmt> stack8 = new MyStack<>();
        IStmt example_8 = new CompStmt(
                new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(
                        new NewStmt("v", new ValueExp(new IntValue(20))),
                        new CompStmt(
                                new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                                new CompStmt(
                                        new NewStmt("a", new VarExp("v")),
                                        new CompStmt(
                                                new NewStmt("v", new ValueExp(new IntValue(30))),
                                                new PrintStmt(new HeapReadingExp(new HeapReadingExp(new VarExp("a"))))
                                        )

                                )
                        )
                )
        );
        try{
            example_8.typecheck(new MyDictionary<String, Type>());
            stack8.push(example_8);
            PrgState prg8 = new PrgState(stack8, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo8 = new Repository(prg8, "log8.txt");
            Controller ctr8 = new Controller(repo8);
            menu.addCommand(new RunExample("8", example_8.toString(), ctr8));
        }
        catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }

        IMyStack<IStmt> stack9 = new MyStack<>();
        IStmt example_9 = new CompStmt(
                new VarDeclStmt("v", new IntType()),
                new CompStmt(
                        new AssignStmt("v", new ValueExp(new IntValue(4))),
                        new CompStmt(
                                new WhileStmt(
                                        new CompStmt(
                                                new PrintStmt(new VarExp("v")),
                                                new AssignStmt("v", new ArithExp('-', new VarExp("v"), new ValueExp(new IntValue(1))))
                                        ), new RelationalExp(5, new VarExp("v"), new ValueExp(new IntValue(0)))
                                ),
                                new PrintStmt(new VarExp("v"))
                        )
                )
        );
        try{
            example_9.typecheck(new MyDictionary<String, Type>());
            stack9.push(example_9);
            PrgState prg9 = new PrgState(stack9, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo9 = new Repository(prg9, "log9.txt");
            Controller ctr9 = new Controller(repo9);
            menu.addCommand(new RunExample("9", example_9.toString(), ctr9));
        }
        catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }


        IMyStack<IStmt> stack10 = new MyStack<>();
        IStmt example_10 = new CompStmt(
                new VarDeclStmt("v", new IntType()),
                new CompStmt(
                        new VarDeclStmt("a", new RefType(new IntType())),
                        new CompStmt(
                                new AssignStmt("v", new ValueExp(new IntValue(10))),
                                new CompStmt(
                                        new NewStmt("a", new ValueExp(new IntValue(22))),
                                        new CompStmt(
                                                new ForkStmt(
                                                        new CompStmt(
                                                                new HeapWritingStmt("a", new ValueExp(new IntValue(30))),
                                                                new CompStmt(
                                                                        new AssignStmt("v", new ValueExp(new IntValue(32))),
                                                                        new CompStmt(
                                                                                new PrintStmt(new VarExp("v")),
                                                                                new PrintStmt(new HeapReadingExp(new VarExp("a")))
                                                                        )
                                                                )
                                                        )
                                                ),
                                                new CompStmt(
                                                        new PrintStmt(new VarExp("v")),
                                                        new PrintStmt(new HeapReadingExp(new VarExp("a")))
                                                )
                                        )
                                )
                        )
                )
        );
        try{
            example_10.typecheck(new MyDictionary<String, Type>());
            stack10.push(example_10);
            PrgState prg10 = new PrgState(stack10, new MyDictionary<String, Value>(), new MyList<Value>(), new FileTable<StringValue, BufferedReader>(), new MyHeap());
            IRepository repo10 = new Repository(prg10, "log10.txt");
            Controller ctr10 = new Controller(repo10);
            menu.addCommand(new RunExample("10", example_10.toString(), ctr10));
        }
        catch (StmtException |  ExprException |  ADTException e){
            System.out.println(e.getMessage());
        }
        menu.addCommand(new ExitCommand("0", "Exit"));
        menu.show();;
    }
}

