package com.example.demo2;

import controller.Controller;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.SelectionMode;
import model.ADT.*;
import model.PrgState;
import model.exception.ADTException;
import model.exception.ExprException;
import model.exception.StmtException;
import model.expression.*;
import model.statement.*;
import model.type.IntType;
import model.type.RefType;
import model.type.StringType;
import model.type.Type;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;
import repository.IRepository;
import repository.Repository;
import view.ExitCommand;
import view.RunExample;

import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.List;

public class SelectController {

    private MainController mainController;
    public void setMainController(MainController mainController){
        this.mainController = mainController;
    }
    @FXML
    private ListView<IStmt> programsListView;

    @FXML
    private Button displayButton;

    @FXML
    public void initialize(){
        programsListView.setItems(getAllStatements());
        programsListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
    }

    @FXML
    private void displayProgram(ActionEvent actionEvent){
        IStmt selectedStatement = programsListView.getSelectionModel().getSelectedItem();
        if (selectedStatement == null){
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error encountered!");
            alert.setContentText("No statement selected!");
            alert.showAndWait();
        }
        else{
            int id  = programsListView.getSelectionModel().getSelectedIndex();
            try{
                selectedStatement.typecheck(new MyDictionary<String, Type>());
                PrgState programState = new PrgState(new MyStack<>(), new MyDictionary<String, Value>(),new MyList<>(), new FileTable<StringValue, BufferedReader>(), new MyHeap(), selectedStatement);
                IRepository repository = new Repository(programState, "log" + (id+1)+".txt");
                Controller controller = new Controller(repository);
                mainController.setController(controller);
            }
            catch (ExprException |  StmtException | ADTException e) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Error encountered!");
                alert.setContentText(e.getMessage());
                alert.showAndWait();
            }
        }
    }

    private ObservableList<IStmt> getAllStatements(){
        List<IStmt> allStatements = new ArrayList<>();

        IStmt example_1 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ValueExp(new IntValue(17))),
                        new PrintStmt(new VarExp("x"))
                )
        );
        allStatements.add(example_1);

        IStmt example2 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ArithExp('+', new ValueExp(new IntValue(5)), new ValueExp(new IntValue(7)))),
                        new PrintStmt(new VarExp("x"))
                )
        );
        allStatements.add(example2);

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
        allStatements.add(example_3);

        IStmt example_4 = new CompStmt(
                new VarDeclStmt("x", new IntType()),
                new CompStmt(
                        new AssignStmt("x", new ValueExp(new BoolValue(false))),
                        new PrintStmt(new VarExp("x"))
                )
        );

        allStatements.add(example_4);

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
        IStmt ex = new CompStmt(
                new VarDeclStmt("varf", new StringType()),
                new CompStmt(
                        new AssignStmt("varf", new ValueExp(new StringValue("test.in"))),
                        new CompStmt(
                                new openRFileStmt(new VarExp("varf")),
                                new CompStmt(
                                        new VarDeclStmt("varc", new IntType()),
                                        new CompStmt(
                                                new readRFileStmt(new VarExp("varf"), "varc"),
                                                new CompStmt(
                                                        new PrintStmt(new VarExp("varc")),
                                                        new CompStmt(
                                                                new readRFileStmt(new VarExp("varf"), "varc"),
                                                                new CompStmt(
                                                                        new PrintStmt(new VarExp("varc")),
                                                                        new closeRFileStmt(new VarExp("varf"))
                                                                )
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );
        allStatements.add(example_5);
        allStatements.add(example_6);
        allStatements.add(example_7);
        allStatements.add(example_8);
        allStatements.add(example_9);
        allStatements.add(example_10);
        allStatements.add(ex);

        return FXCollections.observableArrayList(allStatements);
    }

}