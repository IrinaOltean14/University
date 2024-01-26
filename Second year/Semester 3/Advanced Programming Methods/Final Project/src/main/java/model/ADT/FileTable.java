package model.ADT;

import model.exception.ADTException;

import java.util.HashMap;
import java.util.Map;

public class FileTable<K, V> implements IFileTable<K, V> {
    private Map<K, V> map;

    public FileTable(Map<K, V> map){
        this.map = map;
    }

    public FileTable(){
        map = new HashMap<K, V>();
    }

    @Override
    public V lookup(K key) {
        return map.get(key);
    }

    @Override
    public void update(K key, V value) {
        if (map.containsKey(key))
            map.put(key, value);
    }

    @Override
    public void remove(K key) {
        map.remove(key);
    }

    @Override
    public boolean isDefined(K key) {
        return map.containsKey(key);
    }

    @Override
    public void add(K key, V value) throws ADTException {
        if (map.containsKey(key))
            throw new ADTException("Element already exists");
        this.map.put(key, value);
    }

    @Override
    public Map<K, V> getContent() {
        return map;
    }

    public void setContent(Map<K, V> content){
        this.map = content;
    }

    @Override
    public String toString(){
        return map.toString();
    }
}
