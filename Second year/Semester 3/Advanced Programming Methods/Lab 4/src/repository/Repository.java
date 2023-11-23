package repository;

import model.PrgState;
import model.exception.MyException;

import java.io.*;
import java.util.*;
public class Repository implements IRepository{
    private List<PrgState> states;
    private String logFilePath;

    public Repository(String givenFile){
        this.logFilePath = givenFile;
        states = new ArrayList<>();
    }

    public Repository(PrgState state, String givenFile){
        states = new ArrayList<>();
        states.add(state);
        this.logFilePath = givenFile;
    }

    public Repository(List<PrgState> programList, String filename) throws IOException, MyException{
        states = programList;
        logFilePath = filename;
    }

    public Repository() {
        states = new ArrayList<>();
    }

    public Repository(PrgState state){
        states = new ArrayList<>();
        states.add(state);
    }

    public String getLogFilePath(){
        return logFilePath;
    }

    public void setLogFilePath(String logFilePath){
        this.logFilePath = logFilePath;
    }


    @Override
    public PrgState getCrtPrg() {
        PrgState state = states.get(0);
        states.remove(0);
        return state;
    }

    @Override
    public List<PrgState> getPrgStates() {
        return states;
    }

    public void setPrgList(List<PrgState> l){
        this.states = l;
    }

    @Override
    public void addState(PrgState state) {
        states.add(state);
    }

    @Override
    public void logPrgStateExec(PrgState state) throws MyException, IOException {
        PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        logFile.write(state.toString());
        logFile.close();
    }
}
