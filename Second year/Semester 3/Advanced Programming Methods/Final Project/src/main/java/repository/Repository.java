package repository;

import model.PrgState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
public class Repository implements IRepository{
    private List<PrgState> states;
    private String logFilePath;

    public Repository(PrgState state, String givenFile){
        states = new ArrayList<>();
        states.add(state);
        this.logFilePath = givenFile;
    }

    public void setPrgList(List<PrgState> l){
        this.states = l;
    }

    @Override
    public void addState(PrgState state) {
        states.add(state);
    }

    @Override
    public void logPrgStateExec(PrgState state) throws IOException {
        PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        logFile.write(state.toString());
        logFile.close();
    }

    @Override
    public List<PrgState> getPrgList() {
        return states;
    }
}
