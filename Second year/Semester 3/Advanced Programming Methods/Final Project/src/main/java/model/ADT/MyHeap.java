package model.ADT;

import model.value.Value;

import java.util.HashMap;

public class MyHeap implements IMyHeap{
    private HashMap<Integer, Value> heap;
    private int freeLocation;

    public MyHeap(){
        this.heap = new HashMap<Integer, Value>();
        this.freeLocation = 0;
    }

    public void setFreeLocation(int freeLocation) {
        this.freeLocation = freeLocation;
    }
    @Override
    public void put(int key, Value value) {
        heap.put(key, value);
    }

    @Override
    public Value lookup(int key) {
        return heap.get(key);
    }

    @Override
    public boolean containsKey(int key) {
        return heap.containsKey(key);
    }

    @Override
    public void update(int key, Value value) {
        heap.put(key, value);
    }

    @Override
    public int getFreeAddress() {
        freeLocation += 1;
        return freeLocation;
    }

    @Override
    public void setContent(HashMap<Integer, Value> heap) {
        this.heap = heap;
    }

    @Override
    public HashMap<Integer, Value> getContent() {
        return heap;
    }

    @Override
    public String toString(){
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("Heap:\n");

        for (HashMap.Entry<Integer, Value> entry : heap.entrySet()) {
            stringBuilder.append("  [").append(entry.getKey()).append("] -> ").append(entry.getValue()).append("\n");
        }

        stringBuilder.append("Free Location: ").append(freeLocation + 1).append("\n");

        return stringBuilder.toString();
    }
}
