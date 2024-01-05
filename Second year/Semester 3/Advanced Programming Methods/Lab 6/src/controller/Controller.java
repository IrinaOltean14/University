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

import java.io.IOException;
import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Controller {
    private IRepository repository;
    private ExecutorService executor;

    public Controller(IRepository repository){
        this.repository = repository;
        executor = null;
    }

    public void oneStepForAll(List<PrgState> prgLst) throws InterruptedException {
        prgLst.forEach(prg-> {
            try {
                repository.logPrgStateExec(prg);
            } catch (MyException | IOException e) {
                throw new RuntimeException(e);
            }
        });

        List<Callable<PrgState>> callList = prgLst.stream()
                .map((PrgState p)->(Callable<PrgState>)(()->{return p.oneStep();}))
                .collect(Collectors.toList());

        List<PrgState> newPrgList = executor.invokeAll(callList).stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (InterruptedException | ExecutionException e){
                        throw new RuntimeException(e);
                    }
                })
                .filter(p -> p != null)
                .collect(Collectors.toList());
        prgLst.addAll(newPrgList);
        prgLst.forEach(prg-> {
            try {
                repository.logPrgStateExec(prg);
            } catch (MyException | IOException e) {
                throw new RuntimeException(e);
            }
        });
        repository.setPrgList(prgLst);

    }

    public void allStep() throws MyException, IOException, InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        // remove the completed programs
        List<PrgState> prgList = removeCompletedPrg(repository.getPrgList());
        while (prgList.size() >0){
            prgList
                    .forEach(program -> this.garbageCollector(
                            this.getAddrFromSymTable(program.getDictionary().getContent().values()),
                            program.getHeap().getContent()));
            oneStepForAll(prgList);
            prgList = removeCompletedPrg(repository.getPrgList());
        }
        executor.shutdownNow();
        repository.setPrgList(prgList);
    }


    Map<Integer, Value> garbageCollector(List<Integer> symTableAddr, Map<Integer,Value> heap){
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

    public List<PrgState> removeCompletedPrg(List<PrgState> inPrgList){
        return inPrgList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }

}
