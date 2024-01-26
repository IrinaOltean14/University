package controller;

import model.ADT.*;
import model.PrgState;
import model.exception.MyException;
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

    public List<PrgState> getProgramStates() {
        return this.repository.getPrgList();
    }
    public List<Integer> getAddressesFromSymTable(Collection<Value> symTableValues) {
        return symTableValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue) v; return v1.getAddr();})
                .collect(Collectors.toList());
    }

    public List<Integer> getAddressesFromHeap(Collection<Value> heapValues) {
        return heapValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue) v; return v1.getAddr();})
                .collect(Collectors.toList());
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

    public void oneStep() throws InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        List<PrgState> programStates = removeCompletedPrg(repository.getPrgList());
        oneStepForAll(programStates);
        conservativeGarbageCollector(programStates);
        //programStates = removeCompletedPrg(repository.getProgramList());
        executor.shutdownNow();
        //repository.setProgramStates(programStates);
    }
    public void conservativeGarbageCollector(List<PrgState> programStates) {
        List<Integer> symTableAddresses = Objects.requireNonNull(programStates.stream()
                        .map(p -> getAddressesFromSymTable(p.getDictionary().getContent().values()))
                        .map(Collection::stream)
                        .reduce(Stream::concat).orElse(null))
                .collect(Collectors.toList());
        programStates.forEach(p -> p.getHeap().setContent((HashMap<Integer, Value>) safeGarbageCollector(symTableAddresses, getAddressesFromHeap(p.getHeap().getContent().values()), p.getHeap().getContent())));
    }


    Map<Integer, Value> garbageCollector(List<Integer> symTableAddr, Map<Integer,Value> heap){
        return heap.entrySet().stream().
                filter(e -> symTableAddr.contains(e.getKey()) )
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddresses, List<Integer> heapAddresses, Map<Integer, Value> heap) {
        return heap.entrySet().stream()
                .filter(e -> ( symTableAddresses.contains(e.getKey()) || heapAddresses.contains(e.getKey())))
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

    public IRepository getRepo() {
        return repository;
    }

//    public void oneStepExecution() throws MyException {
//        // we fix the nb of threads
//        executor = Executors.newFixedThreadPool(2);
//        // remove completed programs
//        List<PrgState> programs = removeCompletedPrg(this.repository.getPrgList());
//        if (programs.size() > 0){
//            Collection<Value> addresses = programs.stream().
//                    flatMap(program -> program.getDictionary().getContent().values().stream())
//                    .collect(Collectors.toList());
//            // we apply the safe garbage collector
//            programs.get(0).getHeap().setContent(this.safeGarbageCollector(this.getAddressesFromSymTable(addresses),
//                    this.getAddressesFromHeap(programs.get(0).getHeap().getContent()), programs.get(0)));
//            try{
//                this.oneStepForAll(programs);
//            } catch (InterruptedException e) {
//                throw new MyException("cv");
//            }
//            programs = removeCompletedPrg(this.repository.getPrgList());
//        }
//        executor.shutdown();
//        this.repository.setPrgList(programs);
//    }

    public void setProgramStates(List<PrgState> programStates) {
        this.repository.setPrgList(programStates);
    }
}
