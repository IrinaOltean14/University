package model.ADT;

import model.exception.ADTException;
import model.exception.MyException;
import java.util.*;
public class MyDictionary<K, V> implements IMyDictionary<K, V> {
    private Map<K, V> map;
    public MyDictionary(){
        this.map = new HashMap<>();
    }

    @Override
    public void add(K key, V value) throws ADTException {
        if (map.containsKey(key))
            throw new ADTException("Element already exists");
        this.map.put(key, value);
    }

    @Override
    public boolean isDefined(K key) {
        return map.containsKey(key);
    }

    @Override
    public V lookup(K key) {
        return map.get(key);
    }

    @Override
    public void update(K key, V value) {
        map.put(key, value);
    }

    @Override
    public String toString() {
        StringBuilder content = new StringBuilder();
        for (Map.Entry<K, V> el : map.entrySet()) {
            content.append(el.getKey()).append("-").append(el.getValue()).append(" ");
        }
        return content.toString();
    }

}
