package model.ADT;

import model.exception.ADTException;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
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
    public Map<K, V> getContent() {
        return map;
    }

    @Override
    public String toString() {
        String representation = "[ \n";
        Collection<K> allKeys = map.keySet();
        for(K key: allKeys){
            representation += (key.toString() + ": " + map.get(key) + ", \n");
        }
        representation += "]";
        return representation;
    }

}
